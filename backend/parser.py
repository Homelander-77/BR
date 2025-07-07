import json

class HTTPRequest:    
    def __init__(self, raw_request: str):
        self.raw_request = raw_request.strip()
        self.headers = {}
        self.body = ""
        self.method = ""
        self.path = ""
        self.http_version = ""
        self._parse()
    
    def _parse(self):
        parts = self.raw_request.split('\r\n\r\n', 1)
        headers_section = parts[0]
        if len(parts) > 1:
            self.body = json.loads(parts[1])
        else:
            self.body = ""
        
        # Split headers into lines
        header_lines = headers_section.split('\n')
        # Parse the request line (first line)
        if header_lines:
            request_line = header_lines[0].split(' ')
            if len(request_line) >= 3:
                self.method = request_line[0]
                self.path = request_line[1]
                self.http_version = request_line[2]
        
        # Parse the headers
        for line in header_lines[1:]:
            if ':' in line:
                key, value = line.split(':', 1)
                self.headers[key.strip()] = value.strip()

    def __repr__(self):
        return f"HTTPRequest(method='{self.method}', path='{self.path}', headers={len(self.headers)} items)"

