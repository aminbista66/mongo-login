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
