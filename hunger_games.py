__author__ = 'karnikamit'
string_input = raw_input()
input_list = string_input.split(" ")
input_list = [int(i) for i in input_list]
alphabets = 'abcdefghijklmnopqrstuvwxyz'
alphabets = [i for i in alphabets]
score = dict(zip(alphabets, input_list))
m_score = 0
d_score = 0
Q = int(raw_input())
for game in xrange(Q):
    m_input = raw_input()
    m_list = [m for m in m_input]
    d_input = raw_input()
    d_list = [d for d in d_input]

    for char in m_input:
        for let in d_input:
            if char == let:
                m_input.index(char)
                d_input.index(let)
                d_list.remove(char)
                m_list.remove(let)
                break
    m_score += sum([score[char] for char in m_list])
    d_score += sum([score[let] for let in d_list])
if m_score > d_score:
    print 'Marut'
else:
    print 'Devil'



