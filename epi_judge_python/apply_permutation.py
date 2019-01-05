from test_framework import generic_test


def apply_permutation1(perm, A):
    # TODO - you fill in here.
    for i in range(len(A)):
        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            perm[next] -= len(perm)
            next = temp
    perm[:] = [a + len(perm) for a in A]
    return


def apply_permutation(perm, A):
    def cyclic_permutations(start, A):
        temp_val = A[start]
        index = start
        while True:
            next_index = perm[index]
            next_val = A[next_index]
            A[next_index] = temp_val
            temp_val = next_val
            index = next_index
            if index == start:
                break
    for i in range(len(perm)):
        j = perm[i]
        while j != i:
            if j < i:
                break
            j = perm[j]
        if j == i:
            cyclic_permutations(j, A)


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))
