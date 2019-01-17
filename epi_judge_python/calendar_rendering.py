import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))


def find_max_simultaneous_events(A):
    timings = [p for event in A for p in (Endpoint(event.start, True), Endpoint(event.finish, False))]
    timings.sort(key=lambda x: (x.time, not x.is_start))

    count = 0
    max_count = 0
    for endpoint in timings:
        if endpoint.is_start:
            count += 1
            max_count = max(max_count, count)
        else:
            count -= 1
    # TODO - you fill in here.
    return max_count


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
