from test_framework import generic_test


def search_smallest(A):
    left = 0
    right = len(A) - 1

    def search(left, right):
        # if True or A[0] > A[-1]:
        if left == right:
            return left
        if left > right:
            return -1
        mid = left + (right - left) // 2
        if (mid == 0 and A[mid] < A[mid + 1]) or (mid == len(A) - 1 and A[mid] < A[mid - 1]) or A[mid - 1] > A[mid] < A[mid + 1]:
            return mid
        elif A[mid] < A[right]:
            return search(left, mid - 1)
        elif A[mid] > A[right]:
            return search(mid + 1, right)
        # else:
        #     return 0

    '''while left <= right:
        mid = left + (right - left) // 2
        if (mid == 0 or A[mid - 1]) > A[mid] < (A[mid + 1] or mid == (len(A) - 1)):
            # left = mid
            break
        if A[mid] < A[right]:
            right = mid - 1
        elif A[mid] > A[right]:
            left = mid + 1'''
    # TODO - you fill in here.
    return search(left, right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
