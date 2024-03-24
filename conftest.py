import pytest
from mongomock import MongoClient
from app import create_app
from config import Config

@pytest.fixture
def app():
    mongo = MongoClient(Config.MONGO_URI)
    app = create_app(mongo=mongo)
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def mongo():
    return MongoClient(Config.MONGO_URI)