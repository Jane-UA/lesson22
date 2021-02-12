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
    if a < 0 and n < 1:
        raise ValueError('This function works only with positive integers')
    return mult() +a



