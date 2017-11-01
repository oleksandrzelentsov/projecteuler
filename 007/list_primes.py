from pickle import dump, load


def is_prime(num, cache=None):
    if cache is None:
        cache = {}

    if num in cache:
        return cache.get(num)

    if num <= 1:
        return False

    possible_divisors = list(range(2, int(num / 2)))[::-1]
    for t in possible_divisors:
        if num % t == 0:
            return False

    return True


def primes(cache=None):
    i = 2
    if cache is None:
        cache = {}

    while True:
        cache[i] = is_prime(i, cache)
        if cache[i]:
            yield i

        i += 1



if __name__ == '__main__':
    try:
        with open('cache.dat', 'rb') as c:
            cache = load(c)
    except (IOError, EOFError):
        cache = {}

    p = primes(cache)
    res = []
    for i in range(20000):
        res.append(next(p))

    print(res[-1])

    with open('cache.dat', 'wb') as c:
        dump(cache, c)
