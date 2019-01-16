from test_framework import generic_test


def test_collatz_conjecture(n):
    verified_numbers = set()
    if n == 1 or n == 2:
        return True
    for test_num in range(3, n + 1):
        sequence = set()
        while test_num > 1:
            if test_num in sequence:
                return False
            sequence.add()
            if test_num % 2:
                sequence.add(test_num)

    # TODO - you fill in here.
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("collatz_checker.py",
                                       'collatz_checker.tsv',
                                       test_collatz_conjecture))
