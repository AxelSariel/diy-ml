from flask import Blueprint, jsonify, current_app
from bson.json_util import dumps
from app.utils import get_mongo

bp = Blueprint('users', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    mongo = get_mongo()
    users = mongo.db.users.find()

    print(dumps(users))

    users_json = dumps(users)
    return {'users': users_json}, 200, {'Content-Type': 'application/json'}