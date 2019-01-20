from test_framework import generic_test


def compute_binomial_coefficient(n, k):
    # TODO - you fill in here.
    table = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(n + 1):
        for j in range(k + 1):
            if j == 0 or j == i:
                table[j][i] = 1
            else:
                table[j][i] = table[j - 1][i - 1] + table[j][i - 1]
    return table[k][n]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("binomial_coefficients.py",
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
