from itertools import dropwhile
from difflib import SequenceMatcher
import re

# Steps:
# 1. 8 chars
# 2. small and big letters, special symbols
# 3. easy information or phrases in password

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
path = './common_passwords.txt'


def len_symbols(password: str):
    if re.fullmatch(pattern, password):
        return True, True
    elif len(password) >= 8:
        return True, False
    return False, False


def validate_by_common_list(password: str):
    with open(path) as f:
        for line in dropwhile(lambda x: x.startswith('#'), f):
            common = line.strip().split(':')[-1]
            if common >= 8 and password.lower() == common:
                return False
        return True
