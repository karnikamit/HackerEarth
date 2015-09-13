__author__ = 'karnikamit'

T = int(raw_input())
while T > 0:
    i = int(raw_input())
    my_array = []
    clebs = 0
    while i > 0:
        string_ip = raw_input().split()
        ip_list = [int(k) for k in string_ip]
        if 0 in ip_list:
            clebs += 1
        my_array.append(ip_list)
        i -= 1
    print clebs

    my_array = zip(*my_array)   # getting the transpose'
    index = 0
    for t in my_array:
        m = min([t[item] for item in range(len(t)) if t[item] is not 0])  # determining minimum edge
        print index, t.index(m)
        index += 1

    T -= 1

# 1
# 4
# 3 5 7 0
# 0 8 2 3
# 10 1 9 3
# 4 7 4 0

