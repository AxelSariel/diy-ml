from flask import Flask
from pymongo import MongoClient
from config import Config

def create_app(mongo=None):
    app = Flask(__name__)
    app.config.from_object(Config)
    if mongo is None:
        mongo = MongoClient(Config.MONGO_URI)
    app.mongo = mongo
    register_blueprints(app)
    return app

def register_blueprints(app):
    from app.routes.users import bp as users_bp
    app.register_blueprint(users_bp)

    from app.routes.datasets import bp as datasets_bp
    app.register_blueprint(datasets_bp)

app = create_app()