import string

print(int("4711"), end=' ')
print(string.atoi("4711"), end=' ')
print(string.atoi("11147", 8), end=' ') # octal
print(string.atoi("1267", 16), end=' ') # hexadecimal
print(string.atoi("3mv", 36)) # whatever...

print(string.atoi("4711", 0), end=' ')
print(string.atoi("04711", 0), end=' ')
print(string.atoi("0x4711", 0))

print(float("4711"), end=' ')
print(string.atof("1"), end=' ')
print(string.atof("1.23e5"))

## 4711 4711 4711 4711 4711
## 4711 2505 18193
## 4711.0 1.0 123000.0
