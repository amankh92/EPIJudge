from test_framework import generic_test
from test_framework.test_failure import TestFailure
import collections


class QueueWithMax:
    def __init__(self):
        self._elements = collections.deque()
        self._max = collections.deque()

    def enqueue(self, x):
        self._elements.append(x)
        while self._max and self._max[-1] < x:
            self._max.pop()
        self._max.append(x)
        # TODO - you fill in here.
        return

    def dequeue(self):
        if self._elements:
            result = self._elements.popleft()
            if result == self._max[0]:
                self._max.popleft()
            return result
        raise IndexError('empty queue')
        # TODO - you fill in here.
        # return 0

    def max(self):
        if self._max:
            return self._max[0]
        # TODO - you fill in here.
        return 0


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_with_max.py",
                                       'queue_with_max.tsv', queue_tester))
