from .password import make_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError



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

class UserMixin:
    def __init__(self):
        pass

    def is_authenticated(self):
        print("I am inside is_authenticated()...")

