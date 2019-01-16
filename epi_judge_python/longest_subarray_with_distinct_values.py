from test_framework import generic_test


def longest_subarray_with_distinct_entries(A):
    # TODO - you fill in here.
    mapping = {}
    max_length = float('-inf')
    start = 0
    for index, char in enumerate(A):
        if char not in mapping:
            mapping[char] = index
        else:
            previous_idx = mapping[char]
            if previous_idx >= start:
                length = index - start
                max_length = max(max_length, length)
                start = previous_idx + 1
            mapping[char] = index
    return max(max_length, len(A) - start)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_subarray_with_distinct_values.py",
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
