__author__ = 'karnikamit'

def get_factorials(n):
    fac = 1
    for i in xrange(1, n+1):
        fac *= i
    return fac

cases = int(raw_input())
for case in xrange(cases):
    print get_factorials(int(raw_input()))