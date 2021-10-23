from app.celery import celery_app


@celery_app.task(bind=True)
def test_task(self, a, b):
    return a + b


@celery_app.task(bind=True)
def test_scheduled_task(self, a, b):
    from time import sleep

    sleep(10)
    return a + b
