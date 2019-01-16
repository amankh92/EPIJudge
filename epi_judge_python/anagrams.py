from test_framework import generic_test, test_utils
import collections


def find_anagrams(dictionary):
    def encode(string):
        A = [0] * 58
        for char in string:
            if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
                A[ord(char) - ord('A')] += 1
        return ''.join(str(A))

    mapping = {}
    for word in dictionary:
        key = encode(word)
        if key in mapping:
            mapping[key].append(word)
        else:
            mapping[key] = [word]
    # TODO - you fill in here.
    return [group for group in mapping.values() if len(group) >= 2]


def find_anagras(dictionary):
    mapping = collections.defaultdict(list)
    for s in dictionary:
        mapping[''.join(sorted(s))].append(s)

    return [group for group in mapping.values() if len(group) >= 2]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "anagrams.py",
            "anagrams.tsv",
            find_anagrams,
            comparator=test_utils.unordered_compare))
