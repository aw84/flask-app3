from flask import Flask
from flask_migrate import Migrate

from app.config import DevelopmentConfig
from app.model import db


def create_app(environment=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(environment)
    app.app_context().push()

    db.init_app(app)

    from app.service import api

    api.init_app(app)
    return app


app = create_app()

migrate = Migrate(app, db)
