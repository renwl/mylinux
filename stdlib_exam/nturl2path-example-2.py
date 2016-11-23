import urllib.request, urllib.parse, urllib.error

file = r"c:\my\little\pony"

print(urllib.request.pathname2url(file))
print(urllib.request.url2pathname(urllib.request.pathname2url(file)))

## ///C|/my/little/pony
## C:\my\little\pony
