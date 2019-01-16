from test_framework import generic_test
from test_framework.test_failure import TestFailure
import collections


class LruCache:
    def __init__(self, capacity):
        self._mapping = collections.OrderedDict()
        self._order = [None] * capacity
        self._capacity = capacity
        # TODO - you fill in here.
        return

    def lookup(self, isbn):
        if isbn not in self._mapping:
            return -1
        price = self._mapping.pop(isbn)
        self._mapping[isbn] = price
        # TODO - you fill in here.
        return price

    def insert(self, isbn, price):
        if isbn in self._mapping:
            price = self._mapping.pop(isbn)
        elif len(self._mapping) == self._capacity:
            self._mapping.popitem(last=False)
        self._mapping[isbn] = price
        # TODO - you fill in here.
        return

    def erase(self, isbn):
        # TODO - you fill in here.
        return self._mapping.pop(isbn, None) is not None


def run_test(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    'Lookup: expected ' + str(cmd[2]) + ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    'Erase: expected ' + str(cmd[2]) + ', got ' + str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lru_cache.py", 'lru_cache.tsv',
                                       run_test))
