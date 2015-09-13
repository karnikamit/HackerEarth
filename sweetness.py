__author__ = 'karnikamit'
from random import shuffle
from math import factorial
t = int(raw_input())
while t > 0:
    t -= 1
    no_fruits = int(raw_input())
    ip_fruits = raw_input()
    fruits = [int(i) for i in ip_fruits.split()]
    def get_taste(my_list):
        a_list = list(my_list)
        a_list.insert(0, 0)
        a_list.append(0)
        taste = 2
        for x in xrange(1, len(a_list)):
            try:
                if a_list[x] - a_list[x-1] >= 0:
                    taste += x * (a_list[x] - a_list[x-1])
                else:
                    taste += x * (a_list[x-1] - a_list[x])
            except IndexError:
                pass
        return taste

    f_taste = {}
    temp = []
    for i in xrange(factorial(len(fruits))):
        shuffle(fruits)
        f = fruits
        g = get_taste(f)
        if g not in temp:
            temp.append(g)
            f_taste[i] = g
    print max(f_taste.values())

