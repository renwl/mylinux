import urllib.parse

scheme, host, path, params, query, fragment =\
        urllib.parse.urlparse("http://host/path;params?query#fragment")

if scheme == "http":
    print("host", "=>", host)
    if params:
        path = path + ";" + params
    if query:
        path = path + "?" + query
    print("path", "=>", path)

## host => host
## path => /path;params?query
