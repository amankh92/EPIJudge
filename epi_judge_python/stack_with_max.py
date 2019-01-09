from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    class MaxWithCount:
        def __init__(self, max, count):
            self.max = max
            self.count = count

    def __init__(self):
        self._elements = []
        self._cached_max = []

    def empty(self):
        # TODO - you fill in here.
        return len(self._elements) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        # TODO - you fill in here.
        return self._cached_max[-1].max

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        current_max = self.max()
        popped = self._elements.pop()
        if popped == current_max:
            if self._cached_max[-1].count == 1:
                self._cached_max.pop()
            else:
                self._cached_max[-1].count -= 1
        # TODO - you fill in here.
        return popped

    def push(self, x):
        self._elements.append(x)
        if len(self._cached_max) == 0:
            self._cached_max.append(self.MaxWithCount(x, 1))
        else:
            if x == self.max():
                self._cached_max[-1].count += 1
            elif x > self.max():
                self._cached_max.append(self.MaxWithCount(x, 1))
        # TODO - you fill in here.
        return


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
