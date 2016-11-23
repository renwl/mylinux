import operator
import collections
import numbers

def dump(data):
    print(type(data), "=>", end=' ')
    if hasattr(data, '__call__'):
        print("CALLABLE", end=' ')
    if isinstance(data, collections.Mapping):
        print("MAPPING", end=' ')
    if isinstance(data, numbers.Number):
        print("NUMBER", end=' ')
    if isinstance(data, collections.Sequence):
        print("SEQUENCE", end=' ')
    print()
        
dump(0)
dump("string")
dump("string"[0])
dump([1, 2, 3])
dump((1, 2, 3))
dump({"a": 1})
dump(len) # function
dump(UserList) # module
dump(collections.UserList) # class
dump(collections.UserList()) # instance

## <type 'int'> => NUMBER
## <type 'string'> => SEQUENCE
## <type 'string'> => SEQUENCE
## <type 'list'> => SEQUENCE
## <type 'tuple'> => SEQUENCE
## <type 'dictionary'> => MAPPING
## <type 'builtin_function_or_method'> => CALLABLE
## <type 'module'> =>
## <type 'class'> => CALLABLE
## <type 'instance'> => MAPPING NUMBER SEQUENCE
