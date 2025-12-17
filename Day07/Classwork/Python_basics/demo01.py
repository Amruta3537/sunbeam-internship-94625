def fn():
    l1 = [11,22,33]

    print (l1)

    for value in l1:
        print (value)

    l1.append(44)
    print(l1)
    l1.insert(3,55)
    print(l1)
    l1.pop()
    print(l1)
    l1.remove(22)
    print(l1)

fn()
