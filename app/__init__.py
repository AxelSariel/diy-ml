from flask import Flask
from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost:27017/diyml'

def create_app(mongo=None):
    app = Flask(__name__)
    app.config['MONGO_URI'] = MONGO_URI
    if mongo is None:
        mongo = MongoClient(MONGO_URI)
    app.mongo = mongo
    register_blueprints(app)
    return app

def register_blueprints(app):
    from app.routes.users import bp as users_bp
    app.register_blueprint(users_bp)

app = create_app()