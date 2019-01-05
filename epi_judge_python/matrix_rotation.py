from test_framework import generic_test


def rotate_matrix(square_matrix):
    # TODO - you fill in here.
    size = len(square_matrix) - 1
    for i in range(len(square_matrix) // 2):
        for j in range(i, size - i):
            square_matrix[i][j], square_matrix[j][size - i], square_matrix[size - i][size - j], square_matrix[size - j][
                i] = square_matrix[size - j][i], square_matrix[i][j], square_matrix[j][size - i], \
                     square_matrix[size - i][size - j]
    return


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_rotation.py",
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
