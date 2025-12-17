def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print(f"Addition- {add(a,b)}")
print(f"Substraction- {sub(a,b)}")
print(f"Multiplication- {mul(a,b)}")
print(f"Division- {div(a,b)}")