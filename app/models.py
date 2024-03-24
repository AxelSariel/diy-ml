from app import mongo

class User:
    def __init__(self, userName, userKey):
        self.userName = userName
        self.userKey = userKey