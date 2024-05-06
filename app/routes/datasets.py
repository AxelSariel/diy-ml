import json
from flask import Blueprint, jsonify, current_app, request
from bson.json_util import dumps
from app.utils import getMongo, getJson

bp = Blueprint('datasets', __name__)

@bp.route('/datasets', methods=['GET'])
def get_datasets():
    db = getMongo(current_app)
    datasets = db.datasets.find()
    return jsonify({'datasets': getJson(datasets)})

@bp.route('/datasets/create', methods=['POST'])
def create_dataset():
    db = getMongo(current_app)

    data = request.get_json()
    datasetName = data.get('datasetName')

    if datasetName is None:
        return jsonify({'error': 'datasetName parameter is required'}), 400

    result = db.datasets.insert_one({
        'datasetName': datasetName
    })

    datasetId = str(result.inserted_id)
    
    return jsonify({'datasetId': datasetId}), 201