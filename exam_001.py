class SharedData:
    spam=42

x=SharedData()
y=SharedData()
print(SharedData.spam)
print(x.spam)
print(y.spam)
x.spam=33
print(SharedData.spam)
print(x.spam)
print(y.spam)
SharedData.spam=77
print(SharedData.spam)
print(x.spam)
print(y.spam)
