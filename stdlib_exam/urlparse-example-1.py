import urllib.parse

print(urllib.parse.urlparse("http://host/path;params?query#fragment"))

## ('http', 'host', '/path', 'params', 'query', 'fragment')
