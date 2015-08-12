__author__ = 'karnikamit'

def check(s1, s2):
    [s1.remove(char) for char in s2 if char in s1]
    if s1:
        return "NO"
    else:
        return "YES"
print check(list(raw_input()), list(raw_input()))
