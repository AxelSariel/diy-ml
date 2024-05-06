from app import mongo

class User:
    def __init__(self, userName, userKey):
        self.userName = userName
        self.userKey = userKey

class Dataset:
    def __init__(self, datasetName, datasetLabel):
        self.datasetName = datasetName
        self.datasetLabel = datasetLabel

class Deployment:
    def __init__(self, deploymentName, deployment):
        self.deploymentName = deploymentName