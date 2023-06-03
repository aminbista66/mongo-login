from pymongo.mongo_client import MongoClient
from django.conf import settings
from .validators import user_validator, session_validator

_connection_uri = settings.MONGO_DB['connection_uri']
_client = MongoClient(_connection_uri)
_default_user_colection = 'users'
_db = settings.MONGO_DB['db_name']

def get_db(db_name):
    if db_name is not None:
        return _client[db_name]
    return None

def user_collection(name=_default_user_colection):
    db = get_db(_db)
    if name not in db.list_collection_names(): 
        db.create_collection(name, validator=user_validator)
    return db[name]

def session_collection(name="session"):
    db = get_db(_db)
    if name not in db.list_collection_names():
        db.create_collection(name, validator=session_validator)
        pass
    return db[name]