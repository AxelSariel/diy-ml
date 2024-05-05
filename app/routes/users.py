import json
from flask import Blueprint, jsonify, current_app, request
from bson.json_util import dumps
from app.utils import generateKey, getMongo, getJson

bp = Blueprint('users', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    db = getMongo(current_app)
    users = db.users.find()
    return jsonify({'users': getJson(users)})

@bp.route('/users/create', methods=['POST'])
def create_user():
    db = getMongo(current_app)

    data = request.get_json()
    userName = data.get('userName')

    if userName is None:
        return jsonify({'error': 'userName parameter is required'}), 400
    userKey = generateKey()

    result = db.users.insert_one({
        'userName': userName,
        'userKey': userKey
    })

    userId = str(result.inserted_id)
    
    return jsonify({'userId': userId, 'userKey': userKey}), 201