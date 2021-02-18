
from flask_mongoengine import MongoEngine

db = MongoEngine()

def initialize_db(app):
    db.init_app(app)
    
"""
def save_to_db(cls, data):
    cls.database.stores.insert_one(data)

@classmethod
def load_from_db(cls, query):
    return cls.database.stores.find(query)
"""