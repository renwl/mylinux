import urllib.parse

scheme, host, path, params, query, fragment =\
        urllib.parse.urlparse("http://host/path;params?query#fragment")

if scheme == "http":
    print("host", "=>", host)
    print("path", "=>", urllib.parse.urlunparse((None, None, path, params, query, None)))

## host => host
## path => /path;params?query
