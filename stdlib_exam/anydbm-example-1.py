import dbm

db = dbm.open("database", "c")
db["1"] = "one"
db["2"] = "two"
db["3"] = "three"
db.close()

db = dbm.open("database", "r")
for key in list(db.keys()):
    print(repr(key), repr(db[key]))

## '2' 'two'
## '3' 'three'
## '1' 'one'
