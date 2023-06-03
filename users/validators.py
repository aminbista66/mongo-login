user_validator = {
    '$jsonSchema': {
        'bsonType': 'object',
        'title': 'User Oject Validation',
        'required' : ['password', 'confirm_password', 'email'],
        'properties' : {
            'password': {
                'bsonType': 'string'
            },
            'confirm_password' : {
                'bsonType' : 'string'
            },
            'email' : {
                'bsonType': 'string'
            }
        }
    }
}

session_validator = {
    '$jsonSchema': {
        'bsonType': 'object',
        'title': 'User Oject Validation',
        'required' : ['sid', 'user_id', 'exp'],
        'properties' : {
            'sid': {
                'bsonType': 'string'
            },
            'user_id' : {
                'bsonType' : 'ObjectId'
            },
            'exp' : {
                'bsonType': 'Date'
            }
        }
    }
}