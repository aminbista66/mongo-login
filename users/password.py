from argon2 import PasswordHasher

_hasher = PasswordHasher()

def make_password(password):
    if password is not None:
        return _hasher.hash(password)
    return None
