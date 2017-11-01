from math import floor
from functools import reduce
import unittest


def get_prime_factors(n):
    if n == 1:
        return []
    elif n == 2:
        return [2,]

    for div in range(2, floor(n / 2)):
        if n % div == 0:
            return [div, ] + get_prime_factors(n / div)

    return [n, ]

TEST_DATA = [
    (2, [2,]),
    (12, [2, 2, 3,]),
    (600851475143, [71, 839, 1471, 6857]),
]


class PrimeFactorsUnitTest(unittest.TestCase):
    def test_prime_factors(self):
        for arg, res in TEST_DATA:
            self.assertEqual(get_prime_factors(arg), res)
            self.assertAlmostEqual(reduce(lambda x, y: x * y, res), arg)


if __name__ == '__main__':
    # print(get_prime_factors(int(input('number: '))))
    unittest.main()
