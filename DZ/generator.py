def fib(n):
    x1, x2 = 0, 1
    for i in range(n):
        yield x1
        x1, x2 = x2, x1 + x2


# print(list(fib(5)))
