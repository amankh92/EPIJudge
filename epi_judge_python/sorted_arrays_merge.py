from test_framework import generic_test
import heapq


def merge_sorted_arrays(sorted_arrays):
    min_heap = []
    iterators = [0 for _ in range(len(sorted_arrays))]
    for i in range(len(iterators)):
        heapq.heappush(min_heap, (sorted_arrays[i][iterators[i]], i))
        # iterators[i] += 1
    result = []
    while min_heap:
        smallest, list_id = heapq.heappop(min_heap)
        result.append(smallest)
        iterators[list_id] += 1
        if iterators[list_id] < len(sorted_arrays[list_id]):
            heapq.heappush(min_heap, (sorted_arrays[list_id][iterators[list_id]], list_id))
    # TODO - you fill in here.
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
