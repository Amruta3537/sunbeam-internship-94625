
def extra(fun):
    def inner():
        print("extra")
        fun()
    return inner

@extra
def fun():
    print("fun")


fun()