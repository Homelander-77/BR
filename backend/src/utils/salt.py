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
