from test_framework import generic_test


def examine_buildings_with_sunset(sequence):
    candidates = []
    for id, height in enumerate(sequence):
        while candidates and candidates[-1][1] <= height:
            candidates.pop()
        candidates.append((id, height))
    # TODO - you fill in here.
    return [c[0] for c in reversed(candidates)]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sunset_view.py", 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
