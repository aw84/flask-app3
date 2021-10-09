class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@10.10.0.105:15432/db1"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    DEVELOPMENT = True

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
