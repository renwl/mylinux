import http.cookies
import os, time

cookie = http.cookies.SimpleCookie()
cookie["user"] = "Mimi"
cookie["timestamp"] = time.time()

print(cookie)

# simulate CGI roundtrip
os.environ["HTTP_COOKIE"] = str(cookie)

print()

cookie = http.cookies.SmartCookie()
cookie.load(os.environ["HTTP_COOKIE"])

for key, item in list(cookie.items()):
    # dictionary items are "Morsel" instances
    # use value attribute to get actual value
    print(key, repr(item.value))

## Set-Cookie: timestamp=736513200;
## Set-Cookie: user=Mimi;
##
## user 'Mimi'
## timestamp '736513200'
