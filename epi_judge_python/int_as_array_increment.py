from test_framework import generic_test


def plus_one(A):
    index = len(A) - 1
    carry = 1
    while index >= 0:
        sum_with_carry = A[index] + carry
        carry = int(sum_with_carry / 10)
        sum_without_carry = sum_with_carry % 10
        A[index] = sum_without_carry
        if carry == 0:
            break
        index -= 1
    if carry > 0:
        A = [carry] + A
    # TODO - you fill in here.
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
