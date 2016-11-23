import os

FILES = (
    os.curdir,
    "/",
    "file",
    "/file",
    "samples",
    "samples/sample.jpg",
    "directory/file",
    "../directory/file",
    "/directory/file"
    )

for file in FILES:
    print(file, "=>", end=' ')
    if os.path.exists(file):
        print("EXISTS", end=' ')
    if os.path.isabs(file):
        print("ISABS", end=' ')
    if os.path.isdir(file):
        print("ISDIR", end=' ')
    if os.path.isfile(file):
        print("ISFILE", end=' ')
    if os.path.islink(file):
        print("ISLINK", end=' ')
    if os.path.ismount(file):
        print("ISMOUNT", end=' ')
    print()

## . => EXISTS ISDIR
## / => EXISTS ISABS ISDIR ISMOUNT
## file =>
## /file => ISABS
## samples => EXISTS ISDIR
## samples/sample.jpg => EXISTS ISFILE
## directory/file =>
## ../directory/file =>
## /directory/file => ISABS
