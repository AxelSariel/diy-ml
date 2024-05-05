import json
import string
import secrets
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

def generateKey():
    """Generates a random key for users to authenticate"""
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(32))