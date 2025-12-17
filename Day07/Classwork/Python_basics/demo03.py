# set
def fn():
    s1 = {11,22,33}

    print(s1)

    for value in s1:
        print(value)

    s1.add(44)
    print(s1)

    s1.remove(44)
    print(s1)

    s1.pop()
    print(s1)

fn()

def fn1():
    s1 = {11,22,33}
    s2 = {22,33,44}

    print(s1.union(s2))
    print(s1.intersection(s2))

fn1()