def multiplication(a, b):
    return a * b


def curing(fn, a):
    def new_function(x):
        return fn(x, a)

    return new_function


multiply_by_two = curing(multiplication, 2)

print(multiply_by_two(10))
