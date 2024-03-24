import pytest

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert b'users' in response.data