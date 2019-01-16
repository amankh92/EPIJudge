from test_framework import generic_test
import random


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
    def partition_around_pivot(pivot_index, left, right):
        new_pivot_index = left
        pivot_value = A[pivot_index]
        A[right], A[pivot_index] = A[pivot_index], A[right]
        for i in range(left, right):
            if A[i] > pivot_value:
                A[i], A[new_pivot_index] = A[new_pivot_index], A[i]
                new_pivot_index += 1
        A[new_pivot_index], A[right] = A[right], A[new_pivot_index]
        return new_pivot_index

    left = 0
    right = len(A) - 1
    while left <= right:
        pivot_index = random.randint(left, right)
        next_pivot_index = partition_around_pivot(pivot_index, left, right)
        if next_pivot_index == k - 1:
            return A[next_pivot_index]
        elif next_pivot_index < k - 1:
            left = next_pivot_index + 1
        else:
            right = next_pivot_index - 1
    # TODO - you fill in here.
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
