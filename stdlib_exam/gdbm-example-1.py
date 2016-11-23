import dbm.gnu

db = dbm.gnu.open("gdbm", "c")
db["1"] = "call"
db["2"] = "the"
db["3"] = "next"
db["4"] = "defendant"
db.close()

db = dbm.gnu.open("gdbm", "r")

keys = list(db.keys())
keys.sort()
for key in keys:
    print(db[key], end=' ')

## call the next defendant
