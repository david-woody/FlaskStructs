from flask import Flask
from flask_mongoengine import MongoEngine
from flask_redis import FlaskRedis

from config import config

mongo = MongoEngine()
redis_store = FlaskRedis()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    mongo.init_app(app)
    redis_store.init_app(app)
    ##Regist blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
