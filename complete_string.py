__author__ = 'karnikamit'


def sanitize(function):
    def wrap_function(string, a_list):
        if " " in string:
            string = string.replace(" ", '')
        if '.' in string:
            string = string.replace('.', '')
        if ',' in string:
            string = string.replace(',', '')
        if '-' in string:
            string = string.replace('-', '')
        if '_' in string:
            string = string.replace('_', '')
        return function(string, a_list)
    return wrap_function


# @sanitize
def check(a_string, characters_list):
    if len(a_string) < 26:
        return "NO"
    for char in a_string:
        if characters_list:
            if char in characters_list:
                characters_list.remove(char)
        else:
            return "YES"
    if not characters_list:
        return "YES"
    else:
        return "NO"

cases = int(raw_input(' cases '))
characters = 'abcdefghijklmnopqrstuvwxyz'
characters = list(characters)
for case in xrange(cases):
    ip_string = raw_input('give a string ')
    print check(ip_string, characters)