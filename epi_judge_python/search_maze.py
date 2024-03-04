import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

DIRECTIONS = [
    (-1, 0), # up
    (0, 1), # right
    (1, 0), # down
    (0, -1), # left
]

def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:

    ROWS = len(maze)
    COLS = len(maze[0])
    
    def dfs(coord):
        stack = collections.deque([(coord, [coord])])

        while stack:
            curr_node, curr_path = stack.pop()
            x, y = curr_node.x, curr_node.y
            for dir_x, dir_y in DIRECTIONS:
                new_x, new_y = x + dir_x, y + dir_y
                if 0 <= new_x < ROWS and 0 <= new_y < COLS:
                    next_coord = Coordinate(new_x, new_y)
                    if next_coord.x == e.x and next_coord.y == e.y:
                        return curr_path + [e]
                    elif maze[new_x][new_y] not in [1, 2]:
                        stack.append((next_coord, curr_path + [next_coord]))
                        maze[new_x][new_y] = 2 # mark as visited

        return False
    
    def bfs(coord):
        queue = collections.deque([(coord, [coord])])

        while queue:
            curr_node, curr_path = queue.popleft()

            for dir_x, dir_y in DIRECTIONS:
                new_x, new_y = curr_node.x + dir_x, curr_node.y + dir_y
                new_coord = Coordinate(new_x, new_y)
                if 0 <= new_x < ROWS and 0 <= new_y < COLS:
                    if new_coord == e:
                        return curr_path + [e]
                    elif maze[new_x][new_y] not in [1,2]:
                        queue.append((new_coord, curr_path + [new_coord]))
                        maze[new_x][new_y] = 2 # visited


        return False
    
    return bfs(s)

def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
