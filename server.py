from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'response' : 'Hello world!'
    })

# Users
@app.route('/diyml/users/create', methods=['POST'])
def users_create():
    input = request.get_json
    username = input['username']
    return jsonify({
        'userId' : 'userId_here'
    })

# Projects
@app.route('/diyml/projects/create', methods=['POST'])
def projects_create():
    input = request.get_json
    userId = input['userId']
    projectType = input['projectType']
    projectName = input['projectName']
    return jsonify({
        'projectId' : 'uuid',
        'projectType' : 'project_type',
        'projectName' : 'project_name'
    })

@app.route('/diyml/projects/delete', methods=['POST'])
def projects_delete():
    input = request.get_json
    projectId = input['projectId']
    return jsonify({
        'projectId' : 'uuid'
    })

# Datasets
@app.route('/diyml/datasets/create', methods=['POST'])
def datasets_create():
    input = request.get_json
    projectId = input['projectId']
    datasetType = input['datasetType']
    datasetName = input['datasetName']
    datasetData = input['datasetData']
    datasetMetadata = input['datasetMetadata']
    return jsonify({
        'datasetId' : 'uuid',
        'projectId' : 'uuid',
        'datasetType' : 'dataset_type',
        'datasetName' : 'dataset_name'
    })

@app.route('/diyml/datasets/objects/create', methods=['POST'])
def datasets_objects_create():
    input = request.get_json
    datasetId = input['datasetId']
    objectData = input['objectData']
    objectMetadata = input['objectMetadata']
    return jsonify({
        'datasetId' : 'uuid',
        'objectId' : 'object_id'
    })

@app.route('/diyml/datasets/objects/delete', methods=['POST'])
def datasets_objects_delete():
    input = request.get_json
    datasetId = input['datasetId']
    objectId = input['objectId']
    return jsonify({
        'datasetId' : 'uuid',
        'objectId' : 'object_id'
    })

# PreProcessing
@app.route('/diyml/preprocess', methods=['POST'])
def preprocess():
    input = request.get_json
    datasetId = input['datasetId']
    return jsonify({
        'datasetId' : 'uuid'
    })

# Training
@app.route('/diyml/training/start', methods=['POST'])
def training_start():
    input = request.get_json
    datasetId = input['datasetId']
    trainingParameters = input['trainingParameters']
    return jsonify({
        'trainingJobId' : 'uuid'
    })

@app.route('/diyml/training/status', methods=['GET'])
def training_status():
    input = request.get_json
    trainingJobId = input['trainingJobId']
    return jsonify({
        'trainingJobId' : 'uuid',
        'trainingJobStatus' : 'status_here'
    })

@app.route('/diyml/training/stop', methods=['POST'])
def training_stop():
    input = request.get_json
    trainingJobId = input['trainingJobId']
    return jsonify({
        'trainingJobId' : 'uuid'
    })

@app.route('/diyml/training/results', methods=['GET'])
def training_results():
    input = request.get_json
    trainingJobId = input['trainingJobId']
    return jsonify({
        'trainingJobId' : 'uuid',
        'trainingJobStats' : 'stats_here',
        'trainedModelId' : 'model_id'
    })

# Test
@app.route('/diyml/test/start', methods=['POST'])
def test_create():
    input = request.get_json
    trainedModelid = input['trainedModelid']
    testDatasetId = input['testDatasetId']
    return jsonify({
        'testJobId' : 'uuid'
    })

@app.route('/diyml/test/status', methods=['POST'])
def test_status():
    input = request.get_json
    testJobId = input['testJobId']
    return jsonify({
        'testJobId' : 'uuid',
        'testJobStatus' : 'status_here'
    })

@app.route('/diyml/test/stop', methods=['POST'])
def test_stop():
    input = request.get_json
    testJobId = input['testJobId']
    return jsonify({
        'testJobId' : 'uuid'
    })

@app.route('/diyml/test/results', methods=['GET'])
def test_results():
    input = request.get_json
    testJobId = input['testJobId']
    return jsonify({
        'testJobId' : 'uuid',
        'testJobStats' : 'stats_here'
    })

# Inference
@app.route('/diyml/inference/deploy', methods=['POST'])
def inference_deploy():
    input = request.get_json
    trainedModelId = input['trainedModelId']
    return jsonify({
        'inferenceDeploymentId' : 'inferenceDeploymentId_here'
    })

@app.route('/diyml/inference/delete', methods=['POST'])
def inference_delete():
    input = request.get_json
    inferenceDeploymentId = input['inferenceDeploymentId']
    return jsonify({
        'inferenceDeploymentId' : 'inferenceDeploymentId_here'
    })

@app.route('/diyml/inference/<inferenceDeploymentId>/infer', methods=['POST'])
def inference_infer(inferenceDeploymentId):
    input = request.get_json
    inferenceDeploymentId = input['inferenceDeploymentId']
    inferenceData = input['inferenceData']
    return jsonify({
        'inferenceResults' : 'inferenceResults_here'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0')