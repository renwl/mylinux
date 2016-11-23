import urllib.parse

base = "http://spam.egg/my/little/pony"

for path in "/index", "goldfish", "../black/cat":
    print(path, "=>", urllib.parse.urljoin(base, path))

## /index => http://spam.egg/index
## goldfish => http://spam.egg/my/little/goldfish
## ../black/cat => http://spam.egg/my/black/cat
