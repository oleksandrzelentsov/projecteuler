from math import floor


def is_palindrome(num):
    s = str(num)
    if len(s) % 2 == 0:
        mid = int(len(s) / 2)
        return s[:mid] == s[mid:][::-1]
    else:
        mid = floor(len(s) / 2)
        return s[:mid] == s[mid + 1:][::-1]


if __name__ == '__main__':
    palindromes = sorted([x * y for x in range(100, 1000) for y in range(100, 1000) if is_palindrome(x * y)])
    print(palindromes[-1])
