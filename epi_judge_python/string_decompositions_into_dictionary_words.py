from test_framework import generic_test
import collections


def find_all_substrings(s, words):
    # TODO - you fill in here.
    cache = collections.Counter(words)
    result = [0 for _ in range(len(s))]

    for i in range(0, len(s) - len(''.join(words)) + 1):
        start = i
        end = start + len(''.join(words))
        current_string_freq = collections.Counter()
        flag = 1
        while start < end:
            string = s[start: start + len(words[0])]
            if string not in cache:
                flag = 0
                break
            count = cache[string]
            current_string_freq[string] += 1
            if current_string_freq[string] > count:
                flag = 0
                break
            start = start + len(words[0])
        if flag:
            result[i] = 1
    return [index for index, value in enumerate(result) if value > 0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "string_decompositions_into_dictionary_words.py",
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
