from functools import singledispatch


@singledispatch
def print(x):
    raise TypeError(f"Argument must be of type {x.__class__.__name__}")


@print.register(str)
def print_string(x):
    print(x)


@print.register(int)
def print_int(x):
    print(f"{x}")


@print.register(list)
def print_list(x):
    for element in x:
        print(element)


print("Hallo Welt")
print(1234)
print([1, 2, 3])
