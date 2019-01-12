from test_framework import generic_test
import heapq


def sort_approximately_sorted_array(sequence, k):
    min_heap = []
    for i in range(k + 1):
        try:
            heapq.heappush(min_heap, next(sequence))
        except StopIteration:
            break

    result = []
    for x in sequence:
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)
    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)
    # TODO - you fill in here.
    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
