__author__ = 'karnikamit'


def get_keys(a_list):
    for key in a_list:
        yield key


def merge_keys():
    string_input = raw_input('input ')
    input_list = string_input.split()
    input_list = [int(i) for i in input_list]
    x, orginal_key_value = input_list
    no_keys = int(raw_input('no of keys '))
    string_values = raw_input('values ')
    ip_values = string_values.split()
    ip_values = [int(j.strip()) for j in ip_values]
    count = 0
    for key in get_keys(ip_values):
        count += 1
        temp_key = (x*key) % 100000
        if temp_key == orginal_key_value:
            return count
        else:
            x = temp_key
    return -1


print merge_keys()