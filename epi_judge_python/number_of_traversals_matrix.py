from test_framework import generic_test


def number_of_ways(n, m):
    # TODO - you fill in here.
    table = [[0] * m for _ in range(n)]
    for i in range(n):
        table[i][0] = 1
    for i in range(m):
        table[0][i] = 1
    for i in range(1, n):
        for j in range(1, m):
            table[i][j] = table[i - 1][j] + table[i][j - 1]
    return table[n - 1][m - 1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
