# def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:
# Returns  x ^ exp
# to_power(2, 3) == 8
# True
# to_power(3.5, 2) == 12.25
# True
# to_power(2, -1)
# ValueError: This function works only with exp > 0.
# pass
from typing import Optional


# def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:
#    if x == 0:
#        return 0
#    return to_power(x - 1) * exp
# print(to_power(0,3))
from typing import Optional
def to_power(x, exp):
    if exp == 0:
        return True
    #if exp < 0:
    #   raise ValueError('This function works only with exp > 0')# это исключ. не заботает,
    #   наверное не хватает try|exept
    if exp >= 2:
        return to_power(x, n // 2) * to_power(x, n // 2)

#print(to_power(2,3))


