import os

# where are we?
cwd = os.getcwd()
print("1", cwd)

# go down
os.chdir(r"../")
print("2", os.getcwd())

# go back up
os.chdir(os.pardir)
print("3", os.getcwd())
    
## 1 /ematter/librarybook
## 2 /ematter/librarybook/samples
## 3 /ematter/librarybook
