import hashlib
import os
import binascii


def generate_salt():
    return binascii.hexlify(os.urandom(16)).decode('utf-8')


def salt_password(password: str, salt):
    salted_password = (password + salt).encode('utf-8')
    hash_object = hashlib.sha256(salted_password)
    hashed_password = hash_object.hexdigest()
    return hashed_password


def verify_password(input_login, input_password, database):
    password = database.get_password_by_login(input_login)
    print(input_login, input_password, database)
    if password:
        input_salt = database.get_salt_by_login(input_login)
        input_hash = salt_password(input_password, input_salt)
        return input_hash == password
    else:
        return False
