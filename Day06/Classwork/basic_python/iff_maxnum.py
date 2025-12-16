
a = int(input())
b = int(input())

max = 0

if a == b:
    max=a
    print("both are same")
elif a>b:
    max = a
    print("a is max")
else:
    print("b is max")
    max = b

print("maximum number is - ",max)
