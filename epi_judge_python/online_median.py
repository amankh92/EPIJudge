from test_framework import generic_test
import heapq
import itertools


def online_median(sequence):
    max_heap_left = []
    min_heap_right = []
    median = [next(sequence)]
    heapq.heappush(max_heap_left, -median[-1])
    for x in sequence:
        # if x <= median[-1]:
        if len(max_heap_left) < len(min_heap_right):
            # if x < median[-1]:
            #     heapq.heappush(max_heap_left, -x)
            # else:
            heapq.heappush(max_heap_left, -heapq.heappushpop(min_heap_right, x))
            median.append(0.5 * (-max_heap_left[0] + min_heap_right[0]))
        elif len(max_heap_left) == len(min_heap_right):
            # if x < median[-1]:
            #     heapq.heappush(max_heap_left, -x)
            # else:
            heapq.heappush(max_heap_left, -heapq.heappushpop(min_heap_right, x))
            median.append(-max_heap_left[0])
        else:

            heapq.heappush(min_heap_right, -heapq.heappushpop(max_heap_left, -x))
            median.append(0.5 * (-max_heap_left[0] + min_heap_right[0]))
        # else:

    # TODO - you fill in here.
    return median


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))
