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


async def moss_send(rdocs, language, wildcards, ignore_limit, domain_id, doc_type, tid_str):
    print('moss_send entered')
    tid = bson.objectid.ObjectId(tid_str)

    print('sending moss report...')
    moss_url = await moss.moss_test(rdocs, language=language, wildcards=wildcards, ignore_limit=ignore_limit)
    if moss_url:
        print('Moss report fetched!')
        await contest.update_moss_result(domain_id, doc_type, tid, moss_url=moss_url)
    else:
        print('Moss server failed!')


@app.task
def moss_submit(rdocs, language, wildcards, ignore_limit, domain_id, doc_type, tid_str):
    print('moss_submit entered')
    asyncio.get_event_loop().run_until_complete(
        moss_send(rdocs, language, wildcards, ignore_limit, domain_id, doc_type, tid_str))
