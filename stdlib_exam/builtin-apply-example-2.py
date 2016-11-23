def function(a, b):
    print(a, b)

function(*("crunchy", "frog"))
function(*("crunchy",), **{"b": "frog"})
function(*(), **{"a": "crunchy", "b": "frog"})

## crunchy frog
## crunchy frog
## crunchy frog
