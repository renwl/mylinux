import dbm.dumb

db = dbm.dumb.open("dumbdbm", "c")
db["first"] = "fear"
db["second"] = "surprise"
db["third"] = "ruthless efficiency"
db["fourth"] = "an almost fanatical devotion to the Pope"
db["fifth"] = "nice red uniforms"
db.close()

db = dbm.dumb.open("dumbdbm", "r")
for key in list(db.keys()):
    print(repr(key), repr(db[key]))

## 'first' 'fear'
## 'third' 'ruthless efficiency'
## 'fifth' 'nice red uniforms'
## 'second' 'surprise'
## 'fourth' 'an almost fanatical devotion to the Pope'
