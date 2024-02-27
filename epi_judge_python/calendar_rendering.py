import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    events = [i for event in A for i in [(event.start, True), (event.finish, False)]]
    events.sort(key=lambda e: (e[0], not e[1]))

    max_so_far = 0
    ctr = 0

    for time, is_start in events:
        if is_start:
            ctr += 1
            max_so_far = max(max_so_far, ctr)
        else:
            ctr -= 1

    return max_so_far

@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
