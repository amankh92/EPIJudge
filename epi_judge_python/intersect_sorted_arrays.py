from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    result = []
    iterA = iterB = 0
    while iterA < len(A) and iterB < len(B):
        if A[iterA] == B[iterB]:
            if len(result) == 0 or A[iterA] != result[-1]:
                result.append(A[iterA])
            iterA += 1
            iterB += 1
        elif A[iterA] < B[iterB]:
            iterA += 1
        else:
            iterB += 1

    # TODO - you fill in here.
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
