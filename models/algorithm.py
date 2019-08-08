from db import mongo


class AlgorithmModel:

    def __init__(self):
        self.mongo = mongo

    def insert_algorithm(self, algorithm):
        return mongo.db.suggested_algorithms.insert_one(algorithm)

    def delete_algorithm(self, _id):
        mongo.db.suggested_algorithms.remove({'_id': _id})

    @classmethod
    def find_all(cls):
        return mongo.db.suggested_algorithms.find()