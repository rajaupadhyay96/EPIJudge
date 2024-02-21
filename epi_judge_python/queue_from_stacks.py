from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self) -> None:
        self._stack = []

    def enqueue(self, x: int) -> None:
        self._stack.append(x)

    def dequeue(self) -> int:
        tmp = []
        while self._stack:
            tmp.append(self._stack.pop())

        res = tmp.pop()

        while tmp:
            self._stack.append(tmp.pop())

        return res

def queue_tester(ops):
    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_from_stacks.py',
                                       'queue_from_stacks.tsv', queue_tester))
