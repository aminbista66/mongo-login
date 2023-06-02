# user_validator = {
#     '$jsonSchema': {
#         'bsonType': 'object',
#         'title': 'User Oject Validation',
#         'required' : ['password', 'confirm_password', 'email'],
#         'properties' : {
#             'password': {
#                 'bsonType': 'string'
#             },
#             'confirm_password' : {
#                 'bsonType' : 'string'
#             },
#             'email' : {
#                 'bsonType': 'string'
#             }
#         }
#     }
# }

user_validator = {
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["email", "password", "confirm_passsword"],
            "properties": {
                "email": {
                    "bsonType": "string",
                },
                "password": {
                    "bsonType": "string",
                },
                "confirm_password": {
                    "bsonType": "string",
                },
            }
        }
    }
}
