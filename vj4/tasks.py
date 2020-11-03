import asyncio
import bson
from celery import Celery

from vj4 import constant
from vj4.model import record
from vj4.model.adaptor import moss
from vj4.model.adaptor import contest

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@rabbitmq//')


@app.task
def celery_test():
    print('This is a test for celery...')
    return


async def moss_send(language, wildcards, ignore_limit, domain_id, doc_type, tid_str):
    print('moss_send entered')
    tid = bson.objectid.ObjectId(tid_str)
    tdoc, tsdocs = await contest.get_and_list_status(domain_id, doc_type, tid)
    result = []

    for tsdoc in tsdocs:
        # continue if no record found
        if not tsdoc.get('journal'):
            continue

        rids = list(map(lambda x: x['rid'], tsdoc['journal']))
        rdocs = record.get_multi(get_hidden=True, _id={'$in': rids}).sort([('_id', -1)])

        pids = set(tdoc.get('pids'))
        async for rdoc in rdocs:

            # when all problem have a record, break
            if len(pids) == 0:
                break
            # we only need to get one record for each problem
            if rdoc['pid'] not in pids:
                continue

            pids.remove(rdoc['pid'])
            result.append(rdoc)

    rdocs = result

    print('File fetched, send to MOSS server.')
    moss_url = await moss.moss_test(rdocs, language=language, wildcards=wildcards, ignore_limit=ignore_limit)
    if moss_url:
        print('Moss report fetched!')
        await contest.update_moss_result(domain_id, doc_type, tid, moss_url=moss_url)
    else:
        print('Moss server failed!')


@app.task
def moss_submit(language, wildcards, ignore_limit, domain_id, doc_type, tid_str):
    print('moss_submit entered')
    asyncio.get_event_loop().run_until_complete(
        moss_send(language, wildcards, ignore_limit, domain_id, doc_type, tid_str))
