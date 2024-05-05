import pytest
from app.utils import getJson

def test_get_users(client, db):
    response = client.get('/users')

    currentUsers = getJson(db.users.find())
    expectedResponse = {'users': currentUsers}

    assert response.get_json() == expectedResponse
    assert response.status_code == 200
    assert b'users' in response.data

def test_create_user(client, db):
    response = client.get('/users')

    currentUsers = getJson(db.users.find())
    expectedResponse = {'users': currentUsers}

    assert response.get_json() == expectedResponse
    assert response.status_code == 200
    assert b'users' in response.data