from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # TODO - you fill in here.
    mapping = {}
    for char in magazine_text:
        if char in mapping:
            mapping[char] += 1
        else:
            mapping[char] = 1
    for char in letter_text:
        if char in mapping:
            mapping[char] -= 1
            if mapping[char] == -1:
                return False
        else:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
