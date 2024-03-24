import json
from flask import Blueprint, jsonify, current_app
from bson.json_util import dumps
from app.utils import getMongo, getJson

bp = Blueprint('users', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    db = getMongo(current_app)
    users = db.users.find()
    return jsonify({'users': getJson(users)})