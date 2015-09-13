__author__ = 'karnikamit'
from math import sqrt

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

cases = int(raw_input('cases '))
divisors = []
for case in xrange(cases):
    N = int(raw_input('n '))
    for div in xrange(2, int(sqrt(N))+1):
        if N % div == 0:
            if is_prime(div):
                divisors.append(div)
print divisors