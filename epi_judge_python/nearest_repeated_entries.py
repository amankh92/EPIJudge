from test_framework import generic_test


def find_nearest_repetition(paragraph):
    # TODO - you fill in here.
    min_distance = float('inf')
    cache = {}
    for index, word in enumerate(paragraph):
        if word in cache:
            distance = index - cache[word]
            min_distance = min(distance, min_distance)
            cache[word] = index
        else:
            cache[word] = index
    return min_distance if min_distance < float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
