"""
My solution:
by muliplying all the numbers that have no
divisors, we can get our number
20	4693098009600
19	
18	
17	
16	
15	
14	
13	
12	
11	
7	
"""
def evenly_divisible(number, *numbers):
    return all([number % n == 0 for n in numbers])


if __name__ == '__main__':
    divisors = list(range(1, 16))
    number = 1
    while not evenly_divisible(number, *divisors):
        number += 1
        if number % 1e+6 == 0:
            print('timer', number)

    print(number)
