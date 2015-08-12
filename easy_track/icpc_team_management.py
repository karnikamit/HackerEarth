__author__ = 'karnikamit'


def init_camps():
    string_input = raw_input()
    input_list = string_input.split()
    n, k = [int(i) for i in input_list]
    names = {}
    for i in xrange(n):
        name = raw_input('name ')
        if len(name) in names.keys():
            names[len(name)].append(name)
        else:
            names[len(name)] = []
            names[len(name)].append(name)
    print names

    if n/k == len(names):
        return "Possible"
    else:
        return "Not possible"

cases = int(raw_input())
for case in xrange(cases):
    print init_camps()

# 6 3
# arjit
# tijra
# genius
# chanda
# ashish
# arjit