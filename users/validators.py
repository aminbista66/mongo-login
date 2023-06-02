user_validator = {
    '$jsonSchema': {
        'bsonType': 'object',
        'title': 'User Oject Validation',
        'required' : ['username', 'password', 'confirm_password', 'email'],
        'properties' : {
            'username' : {
                'bsonType': 'string'
            },
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
