from test_framework import generic_test, test_utils


def combinations(n, k):
    # TODO - you fill in here.
    def gen_comb(i, subset_so_far):
        if len(subset_so_far) == k:
            result.append(list(subset_so_far))
            return
        if i > n:
            return
        gen_comb(i + 1, subset_so_far)
        gen_comb(i + 1, subset_so_far + [i])

    result = []
    subset_so_far = []
    gen_comb(1, subset_so_far)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "combinations.py",
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
