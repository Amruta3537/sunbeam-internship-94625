# list of tuple
def fn():
    t1 = [(11,22,33),(44,55,66)]

    print(t1)

    t1.append((77,88,99))
    print(t1)

    t1.pop()
    print(t1)

    t1.remove((11,22,33))
    print(t1)

fn()