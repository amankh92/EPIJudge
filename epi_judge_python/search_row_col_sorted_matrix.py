from test_framework import generic_test


def matrix_search(A, x):
    row_start = 0
    row_end = len(A) - 1
    column_start = 0
    column_end = len(A[0]) - 1
    while row_start <= row_end and column_start <= column_end:
        if x > A[row_start][column_end]:
            row_start += 1
        elif x < A[row_start][column_end]:
            column_end -= 1
        elif x == A[row_start][column_end]:
            return True
    # TODO - you fill in here.
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_row_col_sorted_matrix.py",
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
