import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph, keywords):
    start = 0
    word_set = set()
    min_length = float('inf')
    end = 0
    result = Subarray(-1, -1)
    for i in range(len(paragraph)):
        start = result[1] if result[1] != -1 else i
        while not(keywords < word_set) and start < len(paragraph):
            word_set.add(paragraph[start])
            start += 1
        # if start >= len(paragraph):
        #     break
        length = start - i
        if length < min_length:
            min_length = length
            result = (i, start)
        if paragraph[i] in word_set:
            word_set.remove(paragraph[i])

    # TODO - you fill in here.
    return result


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure("Index out of range")

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure("Not all keywords are in the range")

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_set.py",
            "smallest_subarray_covering_set.tsv",
            find_smallest_subarray_covering_set_wrapper))
