# def sum_of_digits(digit_string: str) -> int:
#    >>> sum_of_digits('26') == 8
#   True
#    >>> sum_of_digits('test')
#   ValueError("input string must be digit string")

import functools

n = list(input())
n = [int(digit) for digit in n]
suma = sum(n)

print("Cумма:", suma)

