from flask import current_app

def get_mongo():
    mongo = current_app.mongo
    if mongo is None:
        raise ValueError('MongoDB connection not provided')
    return mongo