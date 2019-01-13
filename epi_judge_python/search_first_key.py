from test_framework import generic_test


def search_first_of_k(A, k):
    left, right = 0, len(A) - 1
    # result = [[0, float('inf')]]
    # l = []

    def binary_search(left, right):
        if right < left:
            return -1
        mid = left + (right - left) // 2
        if (mid == 0 or k > A[mid - 1]) and A[mid] == k:
            return mid
        elif A[mid] < k:
            return binary_search(mid + 1, right)
        elif A[mid] >= k:
            return binary_search(left, mid - 1)
    # TODO - you fill in here.
    return binary_search(left, right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
