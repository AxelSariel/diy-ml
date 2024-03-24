import json
from bson.json_util import dumps

def getMongo(current_app):
    """Gets MongoDB diyml instance from passed Flask app"""
    mongo = current_app.mongo
    if mongo is None:
        raise ValueError('MongoDB connection not provided')
    return mongo.diyml

def getJson(input):
    """Converts BSON to JSON for MongoDB"""
    return json.loads(dumps(input))