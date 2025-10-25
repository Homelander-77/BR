from itertools import dropwhile
from difflib import SequenceMatcher
import re
import cracklib

from .config import path_conf

# Steps:
# 1. between 8 and 96 chars, login also from 1 to 64
# 2. small and big letters, special symbols
# 3. easy information or phrases in password
# 4. Validation for use as password in other fields, checking on server


def validate_by_len_and_symbols(login: str, password: str):
    lens = {"password": 8 <= password < 96, "login": 6 <= login < 64}
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[.@$!%*#?&/])[A-Za-z\d@$!%*#?&./]{8,}$'
    if re.fullmatch(pattern, password):
        return lens["login"], lens["password"], True
    return lens["login"], lens["password"], False


def validate_by_similarity(firstname: str, lastname: str, mail: str, password: str):
    max_similatiry = 0.4
    fields = re.split(r'\W+', mail) + [firstname, lastname, mail]
    for part in fields:
        diff = SequenceMatcher(a=password.lower(), b=part.lower())
        if diff.ratio() >= max_similatiry:
            return False
    return True


def validate_by_common_list(password: str):
    path = path_conf['common_passwords']
    max_similatiry = 0.7

    with open(path, 'r') as f:
        for line in dropwhile(lambda x: x.startswith('#'), f):
            common = line.strip().split(':')[-1]
            diff = SequenceMatcher(a=password.lower(), b=common)
            if len(common) >= 8 and diff.ratio() >= max_similatiry:
                return False
        return True


def validate_by_common_lib(password: str):
    try:
        cracklib.FascistCheck(password)
        return True
    except ValueError:
        return False


def validate_by_common_combination(password):
    if validate_by_common_lib(password) and validate_by_common_list(password):
        return True
    else:
        return False


def check(firstname: str, lastname: str, login: str, password: str):
    len_password, len_login, symbols = validate_by_len_and_symbols(login, password)
    sim = validate_by_similarity(firstname, lastname, login, password)
    common = validate_by_common_combination(password)

    return {"len_password": len_password, "len_login": len_login, \
            "symbols": symbols, "sim": sim, "common": common}
