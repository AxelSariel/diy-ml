import pytest
from mongomock import MongoClient
from app import create_app

MONGO_URI = 'mongodb://localhost:27017/diyml'

@pytest.fixture
def app():
    mongo = MongoClient(MONGO_URI)
    app = create_app(mongo=mongo)
    app.config['TESTING'] = True
    app.config['MONGO_URI'] = MONGO_URI
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def mongo():
    return MongoClient(MONGO_URI)