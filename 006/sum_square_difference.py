def sum_square_difference(*numbers):
    return abs(sum(numbers) ** 2 - sum(map(lambda x: x ** 2, numbers)))


if __name__ == '__main__':
    print(sum_square_difference(*list(range(1, 101))))
