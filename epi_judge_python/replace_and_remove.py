import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
    write_index = 0
    a_count = 0
    for i in range(size):
        if s[i] != 'b':
            s[write_index] = s[i]
            write_index += 1
        if s[i] == 'a':
            a_count += 1

    cur_index = write_index - 1
    write_index += a_count - 1
    final_size = write_index + 1
    while cur_index >= 0:
        if s[cur_index] == 'a':
            s[write_index - 1: write_index + 1] = 'dd'
            write_index -= 2
        else:
            s[write_index] = s[cur_index]
            write_index -= 1
        cur_index -= 1
    # TODO - you fill in here.
    return final_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
