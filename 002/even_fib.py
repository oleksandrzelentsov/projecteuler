def fibonacci():
    res = [1, 1]
    yield res[0]
    yield res[1]
    while True:
        res.append(res[-2] + res[-1])
        yield res[-1]


if __name__ == '__main__':
    fib = fibonacci()
    res = []
    t = 0
    while t < 4e+6:
        t = next(fib)
        if t % 2 == 0:
            res.append(t)
    print(sum(res))
