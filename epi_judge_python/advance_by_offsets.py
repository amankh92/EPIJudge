from test_framework import generic_test


def can_reach_end(A):
    max_so_far = 0
    for i in range(len(A)):
        if i <= max_so_far:
            max_so_far = max(max_so_far, i + A[i])
    return max_so_far >= (len(A) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
