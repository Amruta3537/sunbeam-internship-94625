def function1(p1, p2, p3):
    print(f"p1 = {p1}, p2 = {p2}, p3 = {p3}")

# function1(10, 20, 30)
# function1(10, 30, 20)
# function1(p1=10, p3=30, p2=20)
# function1(10, 20) #Error

def function2(p1 = 0 , p2 = 0 , p3 = 0):
    print(f"p1 = {p1}, p2 = {p2}, p3 = {p3}")

# function2()
# function2(10, 20, 30)
# function2(10, 20)
# function2(p2=20, p3=30)