import collections
import copy
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze, s, e):

    def find_path(s, e, path = [], visited = set()):
        print(path)
        path.append(e)
        if e == s:
            return path
        if e in visited:
            return None
        visited.add(e)
        next_pts = []
        if e.y + 1 < len(maze[e.x]) and maze[e.x][e.y+1] == WHITE:
            bottom = Coordinate(x = e.x, y = e.y + 1)
            next_pts.append(bottom)
        if e.y - 1 >= 0 and maze[e.x][e.y-1] == WHITE:
            top = Coordinate(x = e.x, y = e.y - 1)
            next_pts.append(top)
        if e.x - 1 >= 0 and maze[e.x-1][e.y] == WHITE:
            left = Coordinate(x = e.x - 1, y = e.y)
            next_pts.append(left)
        if e.x + 1 < len(maze) and maze[e.x+1][e.y] == WHITE:
            right = Coordinate(x = e.x + 1, y = e.y)
            next_pts.append(right)
        if next_pts:
            for pt in next_pts:
                return find_path(s, pt, path, visited)
        else:
            return None

    return find_path(s, e)

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
        raise TestFailure("Path doesn't lay between start and end points")

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure("Path contains invalid segments")

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_maze.py", 'search_maze.tsv',
                                       search_maze_wrapper))
