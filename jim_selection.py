__author__ = 'karnikamit'


def is_odd(num):
    if num > 0:
        if num == 1:
            return True
        if num % 2 == 0:
            return False
        else:
            return True
    else:
        return True     # for this problem

def shortlist(a_list):
    new_list = []
    for i in xrange(len(a_list)):
        if not is_odd(i):
            new_list.append(a_list[i])
    return new_list

def is_power2(num):
    'states if a number is a power of two'
    return num != 0 and ((num & (num - 1)) == 0)

def selection(n):
    if is_power2(n):
        return "Yes"
    else:
        return "No"
    # actors = range(1, n+1)
    # jim = actors[-1]
    # while True:
    #     actors.insert(0, 0)
    #     s_list = shortlist(actors)
    #     if len(s_list) == 1:
    #         if s_list[0] == jim:
    #             return "YES"
    #         return "NO"
    #     actors = s_list

cases = int(raw_input())
for case in xrange(cases):
    print selection(int(raw_input()))
