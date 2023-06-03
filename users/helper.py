from .password import make_password, hasher
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .mongodb import user_collection

def create_user_object(post_object):
    try:
        validate_email(post_object.get('email'))
    except ValidationError:
        raise ValidationError

    if post_object.get('password') != post_object.get('confirm-password'):
        raise Exception('Password Does not match')
    password = make_password(post_object.get('password'))

    user_object = {
        'email' : post_object.get('email'),
        'password': password,
        'confirm_password': password
    }
    return user_object

def authenticate(email, password):
    try:
        user = user_collection().find_one({'email': email})
        if user is None : return None
        hasher.verify(user['password'], password)
        print(user['_id'])
        user_object = {
            'id': user['_id'],
            'email': email,
            'password': password,
            'confirm_password': password
        }
        return user_object
    except Exception as e:
        print(e)
        return None

# TODO : properly structure this code
class User:
    def __init__(self):
        print("I am authenticated user.")
    
    def is_authenticated(self):
        return True

