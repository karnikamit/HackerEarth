__author__ = 'karnikamit'
from math import sqrt


def is_prime(number):
    if number % 2 == 0:
        return False
    for current in range(3, int(sqrt(number) + 1), 2):
        if number % current == 0:
            return False
    return True


from time import time
def get_rev_primes():
    start = time()
    rev_primes = []
    count = 0
    for num in xrange(10, 10**15):
        if time()-start <= 2:
            if is_prime(num):
                b = int(str(num)[::-1])
                if is_prime(b):
                    if b != num and b not in rev_primes:
                        rev_primes.append(num)
                        count += 1
                        print num, count
        else:
            break


get_rev_primes()