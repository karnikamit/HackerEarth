__author__ = 'karnikamit'


def prom_night():
    string_input = raw_input('boys and girls ')
    input_list = string_input.split()
    boys, girls = [int(i) for i in input_list]
    height_input_boy = raw_input('b heights ')
    bhights = height_input_boy.split()
    h_boy = [int(i) for i in bhights]
    height_input_girl = raw_input('g heights ')
    ghights = height_input_girl.split()
    h_girl = [int(i) for i in ghights]
    prom_bheight = dict()
    prom_gheight = dict()
    for boy in xrange(boys):
        prom_bheight[boy] = h_boy[boy]
    for girl in xrange(girls):
        prom_gheight[girl] = h_girl[girl]
    heightsb = sorted(prom_bheight.items(), key=lambda x: x[1], reverse=False)
    count = 0
    print 'ori', prom_gheight
    for i in heightsb:
        for key in prom_gheight:
            if i[1] > prom_gheight[key]:
                print key
                count += 1
                prom_gheight.pop(key, None)
                print prom_gheight
                break
    if count == boys:
        return 'YES'
    else:
        return 'NO'

cases = int(raw_input('cases '))
for case in xrange(cases):
    print prom_night()
