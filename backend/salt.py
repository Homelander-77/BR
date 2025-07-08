import hashlib
import os
import binascii


def generate_salt():
    return binascii.hexlify(os.urandom(16)).decode('utf-8')


def salt_password(password: str):
    salted_password = password.encode('utf-8') + generate_salt()
    hash_object = hashlib.sha256(salted_password)
    hashed_password = hash_object.hexdigest(hash_object)
    return hashed_password

def verify_password(password, psql):
    input_password = 
    salt = 
    input_hash = salt_password(password)
    return input_hash == input_password

