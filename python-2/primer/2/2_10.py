a = 19
print("please input a int number in 1-100")
x = input()
while x != a:
    print("sorry error: \n input again:")
    x = input()
if x == a:
    print("you are right")
    break
input()
