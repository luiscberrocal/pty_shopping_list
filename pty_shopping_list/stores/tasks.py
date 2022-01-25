from time import sleep

from config import celery_app


@celery_app.task()
def sleep_a_little(time):
    sleep(time)
    return 'Done'
