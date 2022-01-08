class CeleryConfig:
    worker_concurrency = 1
    beat_schedule = {
        "add-every-10-seconds": {
            "task": "app.celery.tasks.test_scheduled_task",
            "schedule": 10.0,
            "args": (12, 2),
            "options": {"expires": 2},
        },
    }


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@databse:15432/db1"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    DEVELOPMENT = True
    CELERY_BROKER_URL = "redis://redis:16379/0"
    RESULT_BACKEND = "redis://redis:16379/0"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
