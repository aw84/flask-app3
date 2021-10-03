from flask import Flask
from flask_migrate import Migrate

from app.config import DevelopmentConfig
from app.model import db
from app.service import api


def create_app(environment=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(environment)
    db.init_app(app)
    api.init_app(app)

    return app


app = create_app()
migrate = Migrate(app, db)
