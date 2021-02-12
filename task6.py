# a = 506
def long_dig(a):
    if a < 10:
        return 1
    return long_dig(a // 10) + 1


def mix_integer(a):
    eger = a % 10
    res = a // 10
    step = long_dig(res)
    return 10 ** step * eger + res

assert mix_integer(506) == 650
assert mix_integer(1200) == 120