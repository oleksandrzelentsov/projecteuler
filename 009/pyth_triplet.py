def is_pythagoran_triple(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


if __name__ == '__main__':
    t = [
        (a, b, c)
        for a in range(1, 1000)
        for b in range(1, 1000)
        for c in range(1, 1000)
        if a < b < c and is_pythagoran_triple(a, b, c) and print(a, b, c) is None
    ]
    t = [(a, b, c) for a, b, c in t if a + b + c == 1000 and print(a, b, c) is None]
    for triple in t:
        print("{} + {} + {} = 1000".format(*triple))

