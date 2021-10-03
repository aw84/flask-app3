import pytest
from app import create_app, db
from app.config import TestingConfig


@pytest.fixture(scope="session")
def database():
    try:
        yield db
    finally:
        db.session.remove()
        db.drop_all()


@pytest.fixture(scope="module")
def client(database):
    app = create_app(TestingConfig)
    with app.test_client() as client:
        with app.app_context() as ctx:
            ctx.push()
            database.create_all()
            yield client
