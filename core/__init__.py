from flask import Flask
from core.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
migrate = Migrate()
marshmallow = Marshmallow()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    marshmallow.init_app(app=app)

    with app.app_context():
        return app
