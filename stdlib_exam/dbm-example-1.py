import dbm.ndbm

db = dbm.ndbm.open("dbm", "c")
db["first"] = "bruce"
db["second"] = "bruce"
db["third"] = "bruce"
db["fourth"] = "bruce"
db["fifth"] = "michael"
db["fifth"] = "bruce" # overwrite
db.close()

db = dbm.ndbm.open("dbm", "r")
for key in list(db.keys()):
    print(repr(key), repr(db[key]))

## 'first' 'bruce'
## 'second' 'bruce'
## 'fourth' 'bruce'
## 'third' 'bruce'
## 'fifth' 'bruce'

