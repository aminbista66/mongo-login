from argon2 import PasswordHasher

hasher = PasswordHasher()

def make_password(password):
    if password is not None:
        return hasher.hash(password)
    return None

