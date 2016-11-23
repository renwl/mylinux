import dbm

filename = "database"

result = dbm.whichdb(filename)

if result:
    print("file created by", result)
    handler = __import__(result)
    db = handler.open(filename, "r")
    print(list(db.keys()))
else:
    # cannot identify data base
    if result is None:
        print("cannot read database file", filename)
    else:
        print("cannot identify database file", filename)
    db = None
