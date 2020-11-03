from celery import Celery
import time

from vj4.util import options

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@{}//'.format(options.mq_host))

@app.task
def celery_test():
    print('This is a test for celery...')
    time.sleep(1)
    print('Slept for 1 second...')
    return
