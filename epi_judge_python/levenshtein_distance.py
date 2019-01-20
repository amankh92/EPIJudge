from test_framework import generic_test


def levenshtein_distance(A, B):
    # TODO - you fill in here.
    table = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]
    for iterB in range(len(B) + 1):
        for iterA in range(len(A) + 1):
            if iterB == 0:
                table[iterB][iterA] = iterA
            elif iterA == 0:
                table[iterB][iterA] = iterB
            else:
                if A[iterA - 1] == B[iterB - 1]:
                    table[iterB][iterA] = table[iterB - 1][iterA - 1]
                else:
                    deletion = table[iterB][iterA - 1]
                    insertion = table[iterB - 1][iterA]
                    substitution = table[iterB - 1][iterA - 1]
                    table[iterB][iterA] = 1 + min(deletion, insertion, substitution)
    return table[len(B)][len(A)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))
