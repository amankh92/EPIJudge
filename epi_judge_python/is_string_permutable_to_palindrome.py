from test_framework import generic_test


def can_form_palindrome(s):
    mapping = set()
    for char in s:
        if char in mapping:
            mapping.remove(char)
        else:
            mapping.add(char)
    # TODO - you fill in here.
    if len(s) % 2 == 0:
        return len(mapping) == 0
    else:
        return len(mapping) == 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
