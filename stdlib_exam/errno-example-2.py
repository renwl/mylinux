import errno

try:
    fp = open("no.such.file")
except IOError as xxx_todo_changeme:
    (error, message) = xxx_todo_changeme.args
    print(error, repr(message))
    print(errno.errorcode[error])

# 2 'No such file or directory'
# ENOENT
