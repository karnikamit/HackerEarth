__author__ = 'karnikamit'


def get_feel():
    string_input = raw_input('dress ')
    input_list = string_input.split()
    n, x = [int(i) for i in input_list]
    input_prices = raw_input('price ')
    price_list = input_prices.split()
    if n > x:
        if n - x == 0:
            return "Perfect husband"
        elif n - x < n:
            return "Lame husband"
    else:
        return "Bad husband"

cases = int(raw_input())
for case in range(cases):
    print get_feel()
