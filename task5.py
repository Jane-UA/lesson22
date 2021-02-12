# def sum_of_digits(digit_string: str) -> int:
#    >>> sum_of_digits('26') == 8
#   True
#    >>> sum_of_digits('test')
#   ValueError("input string must be digit string")

def sum_of_digit(digit_string):
    if len(digit_string) == 1:
        return int(digit_string)
    if not digit_string:
        return 0
    return int(digit_string[0]) + sum_of_digit(digit_string[1:])


assert sum_of_digit('123') == 6
