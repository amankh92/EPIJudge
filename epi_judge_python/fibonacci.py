from test_framework import generic_test


def fibonacci(n):
    if n <= 1:
        return n
    a = 0
    b = 1
    for _ in range(1, n):
        c = a
        a = b
        b = c + b
    return b
    # TODO - you fill in here.


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("fibonacci.py", 'fibonacci.tsv',
                                       fibonacci))
