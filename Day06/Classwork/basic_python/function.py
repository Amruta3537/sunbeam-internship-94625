def fn1():
    print("parameterless function")

fn1()

def fn2(a):
    print(f"parameterized function - {a}")

fn2(10)


def sum(a,b):
    sum = a + b
    return sum

Addition = sum(10,20)
print(f"Addition of a & b = {Addition}")