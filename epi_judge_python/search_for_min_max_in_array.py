import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max(A):
    global_min = float('inf')
    global_max = float('-inf')
    for i in range(0, len(A), 2):
        if i == len(A) - 1:
            break
        if A[i] > A[i + 1]:
            global_max = max(global_max, A[i])
            global_min = min(global_min, A[i + 1])
        else:
            global_max = max(global_max, A[i + 1])
            global_min = min(global_min, A[i])
    if len(A) % 2:
        global_max = max(global_max, A[-1])
        global_min = min(global_min, A[-1])

    # TODO - you fill in here.
    return MinMax(global_min, global_max)


def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_for_min_max_in_array.py",
            'search_for_min_max_in_array.tsv',
            find_min_max,
            res_printer=res_printer))
