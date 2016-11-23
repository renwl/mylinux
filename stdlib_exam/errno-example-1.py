import errno

try:
    fp = open("no.such.file")
except IOError as xxx_todo_changeme:
    (error, message) = xxx_todo_changeme.args
    if error == errno.ENOENT:
        print("no such file")
    elif error == errno.EPERM:
        print("permission denied")
    else:
        print(message)

## no such file
