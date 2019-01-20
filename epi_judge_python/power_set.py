from test_framework import generic_test, test_utils


def generate_power_set(S):
    # TODO - you fill in here.
    def gen_power_set(index, subset_so_far):
        if index == len(S):
            result.append(subset_so_far.copy())
            return
        gen_power_set(index + 1, subset_so_far)
        gen_power_set(index + 1, subset_so_far + [S[index]])
    result = []
    subset_so_far = []
    gen_power_set(0, subset_so_far)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
