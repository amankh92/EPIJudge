import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))


def find_duplicate_missing(A):
    # TODO - you fill in here.
    xor_array = 0
    for x in A:
        xor_array ^= x

    xor_all = 0
    for i in range(1, len(A)):
        xor_all ^= i

    xor_final = xor_all ^ xor_array

    set_bit_num = xor_final & ~(xor_final - 1)
    x_0 = 0
    for i, x in enumerate(A):
        if x & set_bit_num:
            x_0 ^= x
        if i & set_bit_num:
            x_0 ^= i
    x_0 ^= xor_final
    if x_0 in set(A):
        y_0 = x_0 ^ xor_final
    else:
        y_0 = x_0
        x_0 ^= xor_final
    return DuplicateAndMissing(x_0, y_0)


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_for_missing_element.py",
            'find_missing_and_duplicate.tsv',
            find_duplicate_missing,
            res_printer=res_printer))
