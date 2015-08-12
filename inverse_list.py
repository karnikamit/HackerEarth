__author__ = 'karnikamit'
cases = int(raw_input())
while cases > 0:
    ip_int = int(raw_input())
    int_list = [int(i) for i in raw_input().split()]
    int_list.insert(0, 0)
    if ip_int == int_list[ip_int]:
        print 'inverse'
    else:
        print "not inverse"
    cases -= 1