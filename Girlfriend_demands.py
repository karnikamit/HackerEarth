__author__ = 'karnikamit'

s = raw_input()
str_len = len(s)
cases = int(raw_input())
for case in range(cases):
    a, b = raw_input().split()
    a, b = int(a), int(b)
    a %= str_len
    b %= str_len
    # try:
    print s[a-1], s[b-1]
    if s[a-1] == s[b-1]:
        print "Yes"
    else:
        print "No"
