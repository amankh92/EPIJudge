from test_framework import generic_test


def multiply(num1, num2):
    # TODO - you fill in here.
    result_length = len(num1) + len(num2)
    result = [0] * result_length
    p_carry = 0
    s_carry = 0
    level = 0
    sign = 1 if (num1[0] * num2[0]) > 0 else -1
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])

    for i in reversed(range(len(num2))):
        for j in reversed(range(len(num1))):
            # result[i + j + 1] += num1[j] * num2[i]
            # result[i + j] += result[i + j + 1] // 10
            # result[i + j + 1] %= 10
            prod = num1[j] * num2[i] + p_carry
            p_carry = prod // 10
            p_sum = prod % 10
            temp_sum = p_sum + result[i + j + 1] + s_carry
            result[i + j + 1] = temp_sum % 10
            s_carry = temp_sum // 10
        if p_carry > 0:
            result[i + j] += p_carry
        p_carry = 0
        if s_carry > 0:
            result[i + j] += s_carry
        s_carry = 0
        # if result[i + j] > 10:
        #     result[i + j - 1] += result[i + j] // 10
        #     result[i + j] = result[i + j] % 10

    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
