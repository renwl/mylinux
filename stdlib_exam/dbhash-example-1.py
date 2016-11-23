import dbm.bsd

db = dbm.bsd.open("dbhash", "c")
db["one"] = "the foot"
db["two"] = "the shoulder"
db["three"] = "the other foot"
db["four"] = "the bridge of the nose"
db["five"] = "the naughty bits"
db["six"] = "just above the elbow"
db["seven"] = "two inches to the right of a very naughty bit indeed"
db["eight"] = "the kneecap"
db.close()

db = dbm.bsd.open("dbhash", "r")
for key in list(db.keys()):
    print(repr(key), repr(db[key]))
