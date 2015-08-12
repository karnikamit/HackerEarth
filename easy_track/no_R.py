__author__ = 'karnikamit'



def count_r():
    string_input = raw_input('ip string ')
    input_list = list(string_input)
    list_len = len(input_list)
    if input_list[0] == 'R':
        r = 1
    else:
        r = 0
    if input_list[-1] == 'R':
        r += 1
    for i in xrange(1, list_len):
        if input_list[i] != 'R':
            r += 1
    return r

case = int(raw_input('cases '))
for ca in range(case):
    print count_r()