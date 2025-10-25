from itertools import dropwhile
from difflib import SequenceMatcher
import re
import cracklib

from .config import path_conf

# Steps:
# 1. 8 chars
# 2. small and big letters, special symbols
# 3. easy information or phrases in password
# 4. Validation for use as password in other fields, checking on server


def validate_by_len_symbols(password: str):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[.@$!%*#?&/])[A-Za-z\d@$!%*#?&./]{8,}$'

    if re.fullmatch(pattern, password):
        return True, True
    elif len(password) >= 8:
        return True, False
    return False, False


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


def check(firstname: str, lastname: str, mail: str, password: str):
    length, symbols = validate_by_len_symbols(password)
    sim = validate_by_similarity(firstname, lastname, mail, password)
    common = validate_by_common_combination(password)

    return {"length": length, "symbols": symbols, "sim": sim, "common": common}
