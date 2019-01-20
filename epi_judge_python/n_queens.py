from test_framework import generic_test


def n_queens(n):

    def is_safe(row, col):
        return all(abs(c - col) not in (0, row - i) for i, c in enumerate(column_placement[:row]))

    def place_queens(row):
        if row == len(column_placement):
            result.append(column_placement.copy())
            return
        for col in range(n):
            if is_safe(row, col):
                column_placement[row] = col
                place_queens(row + 1)
    result, column_placement = [], [0] * n
    place_queens(0)
    # TODO - you fill in here.
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("n_queens.py", 'n_queens.tsv', n_queens,
                                       comp))
