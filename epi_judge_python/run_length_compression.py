from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s):
    result = []
    count = 0
    for char in s:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            result += [count * char]
            count = 0
    # TODO - you fill in here.
    return ''.join(result)


def encoding(s):
    # sentinel = s[0]
    i = 1
    count = 1
    result = []
    while i < len(s):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += [str(count) + s[i - 1]]
            count = 1
        i += 1
    result += [str(count) + s[-1]]
    # print(result)
    # TODO - you fill in here.
    return ''.join(result)


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    # print(encoding("zzzzzzzzzzzzzzzffffzzzzzzzzzznnnnnnnnnnnnnnnsssssssssnnnnnnrrrrrrrrrrrraaaaaaaaaaaaaaaaaaaaaaoooooooooooooooooeeeeeeeeeeeeeeeeeiiiiiiiiiillllllllliiiiiiiiiiiinnnnnnnnnmmmmmmmmmffffhhhhhhhhhhhhhhhhhhhhhhhhxxxxxxxxvvvvvvvvvvvvvvvvvviuuuuuuuuuuuuuuuuuuuuuuubbbbbbbbbbbbbbbbbbbbbbbbbhkkkkkkkkkkkkkkkjjjjjjjjjjjjj"))
    exit(
        generic_test.generic_test_main("run_length_compression.py",
                                       'run_length_compression.tsv',
                                       rle_tester))
