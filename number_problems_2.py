import math


def roman_numeral(n):
    symbol = ['I', 'IV', 'V', 'IX', 'X', 'XL',
              'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    value = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    out = []
    total = n
    for i in range(len(symbol)-1, -1, -1):
        while (total - value[i]) >= 0:
            total = total - value[i]
            out.append(symbol[i])
    return ''.join(out)


def total_roman(n):
    n = roman_numeral(n)
    total = 0
    symbol = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    value = [1, 5, 10, 50, 100, 500, 1000]
    for i in range(0, len(symbol)):
        while symbol[i] in n:
            n = n.replace(symbol[i], '', 1)
            total += value[i]
    return total


def chisel_strokes(n):
    pass


def describe(n):
    pass


def binary_without_zeros(n):
    pass


print(total_roman(6))
