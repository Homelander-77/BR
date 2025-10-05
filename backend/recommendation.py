import json
from response import MakeHTTPResponse


def rec(request, psql):
    ans = json.dumps(psql.get_rec())
    
