from parser import HTTPRequest

a = HTTPRequest('''GET /api/profile HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Accept: application/json
Cookie: id=abc123; theme=dark
Connection: keep-alive''')
print(a.headers)
