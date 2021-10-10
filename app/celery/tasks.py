import flask
from app.celery import celery_app


@celery_app.task(bind=True)
def test_task(self, a, b):
    return a + b


@celery_app.task(bind=True)
def test_scheduled_task(self, a, b):
    from time import sleep
    sleep(10)
    return a + b


# @celery_app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(10.0, test_scheduled_task.s(2, 7), name="add every 10")
