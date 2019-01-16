from test_framework import generic_test


def merge_two_sorted_arrays(A, m, B, n):
    end = m + n - 1
    iterA = m - 1
    iterB = n - 1
    while iterA >= 0 and iterB >= 0:
        if A[iterA] > B[iterB]:
            A[end] = A[iterA]
            end -= 1
            iterA -= 1
        else:
            A[end] = B[iterB]
            end -= 1
            iterB -= 1
    if iterA < 0:
        A[:iterB + 1] = B[:iterB + 1]

    # TODO - you fill in here.
    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sorted_arrays_merge.py",
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
