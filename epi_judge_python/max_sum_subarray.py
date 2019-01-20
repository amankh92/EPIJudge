from test_framework import generic_test


def find_maximum_subarray(A):
    max_ending_here = float('-inf')
    max_so_far = float('-inf')
    for num in A:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    # TODO - you fill in here.
    return max(max_so_far, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_sum_subarray.py",
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
