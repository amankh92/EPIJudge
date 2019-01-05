from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    spiral_order = []
    i = j = 0
    dir = 0
    direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
    for _ in range(len(square_matrix) ** 2):
        spiral_order.append(square_matrix[i][j])
        square_matrix[i][j] = 0
        next_i = i + direction[dir][0]
        next_j = j + direction[dir][1]
        if next_i < 0 or next_j < 0 or next_i >= len(square_matrix) or next_j >= len(square_matrix) or square_matrix[next_i][next_j] == 0:
            dir = (dir + 1) % 4
            next_i = i + direction[dir][0]
            next_j = j + direction[dir][1]
        i, j = next_i, next_j
    # TODO - you fill in here.
    return spiral_order


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
