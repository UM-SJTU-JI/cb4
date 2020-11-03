import asyncio
from celery import Celery

from vj4.model.adaptor import moss
from vj4.model.adaptor import contest

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@rabbitmq//')


@app.task
def celery_test():
    print('This is a test for celery...')
    return


@app.task
def moss_submit(rdocs, language, wildcards, ignore_limit, domain_id, doc_type, tid):
    moss_url = await moss.moss_test(rdocs, language=language, wildcards=wildcards, ignore_limit=ignore_limit)
    if moss_url:
        await contest.update_moss_result(domain_id, doc_type, tid, moss_url=moss_url)
