import pytest
from app.utils import getJson

def test_get_datasets(client, db):
    response = client.get('/datasets')

    currentdatasets = getJson(db.datasets.find())
    expectedResponse = {'datasets': currentdatasets}

    assert response.get_json() == expectedResponse
    assert response.status_code == 200
    assert b'datasets' in response.data

def test_create_dataset(client, db):
    response = client.get('/datasets')

    currentdatasets = getJson(db.datasets.find())
    expectedResponse = {'datasets': currentdatasets}

    assert response.get_json() == expectedResponse
    assert response.status_code == 200
    assert b'datasets' in response.data