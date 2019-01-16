from test_framework import generic_test


def longest_contained_range(A):
    # TODO - you fill in here.
    mapping = {k: 0 for k in A}
    max_length = float('-inf')
    for num in mapping.keys():
        if (num - 1) not in mapping:
            i = num
            while i in mapping:
                mapping[num] += 1
                # mapping.pop(num)
                i = i + 1
            max_length = max(max_length, mapping[num])
    return max_length


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("longest_contained_interval.py",
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
