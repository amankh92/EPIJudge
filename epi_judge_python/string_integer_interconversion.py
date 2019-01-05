from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    neg = False
    if x < 0:
        x = -x
        neg = True
    string = ''
    if x == 0:
        return "0"
    while x > 0:
        num = x % 10
        string += str(num)
        x = x // 10
    # TODO - you fill in here.
    return ('-' if neg else '') + string[::-1]


def string_to_int(s):
    # TODO - you fill in here.
    number = 0
    sign = 1
    for char in s:
        if char == '-':
            sign = -1
            continue
        number *= 10
        number += int(char)
    return number * sign


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
