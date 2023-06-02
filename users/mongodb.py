from pymongo.mongo_client import MongoClient
from django.conf import settings

_connection_uri = settings.MONGO_DB['connection_uri']
_client = MongoClient(_connection_uri)

def establish_connection_to_db(db):
    return _client[db]