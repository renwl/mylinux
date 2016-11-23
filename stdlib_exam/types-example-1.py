import types

def check(object):
    print(object, end=' ')
    if type(object) is int:
        print("INTEGER", end=' ')
    if type(object) is float:
        print("FLOAT", end=' ')
    if type(object) is bytes:
        print("STRING", end=' ')
    if type(object) is type:
        print("CLASS", end=' ')
    if type(object) is types.InstanceType:
        print("INSTANCE", end=' ')
    print()

check(0)
check(0.0)
check("0")

class A:
    pass

class B:
    pass

check(A)
check(B)

a = A()
b = B()

check(a)
check(b)

## 0 INTEGER
## 0.0 FLOAT
## 0 STRING
## A CLASS
## B CLASS
## <A instance at 796960> INSTANCE
## <B instance at 796990> INSTANCE
