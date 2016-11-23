import shelve

db = shelve.open("database", "c")
db["one"] = 1
db["two"] = 2
db["three"] = 3
db.close()

db = shelve.open("database", "r")
for key in list(db.keys()):
    print(repr(key), repr(db[key]))

## 'one' 1
## 'three' 3
## 'two' 2
