from test_framework import generic_test


def is_well_formed(s):
    stack = []
    lookup = {
        '{': '}',
        '[': ']',
        '(': ')'
    }
    for char in s:
        if char in lookup.keys():
            stack.append(char)
        elif char in lookup.values():
            if not stack or lookup[stack.pop()] != char:
                return False
    # TODO - you fill in here.
    return not stack


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
