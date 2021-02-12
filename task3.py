# def mult(a: int, n: int) -> int:
#   """
#    This function works only with positive integers
#    >>> mult(2, 4) == 8
#    True
#    >>> mult(2, 0) == 0
#    True
#    >>> mult(2, -4)
#    ValueError("This function works only with positive integers")
from typing import Optional


def mult(a: int, n: int) -> int:
    if n < 0:
        raise ValueError('This function works only with positive integers')
    if n == 0:
        return 0
    return a + mult(a, n - 1)
assert mult(5,3) == 15
