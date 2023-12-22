import functools
from collections import namedtuple
from heapq import heappop, heappush
import numpy as np


if __name__ == "__main__":
    exit()


def base_convert(num, base, size=0) -> list[int]:
    """
    Converts num to base number.
    :param num: Number to convert
    :param base: Base of conversion
    :param size: size of returned list
    :return:
    """
    _result = []
    while num > 0:
        _result.insert(0, num % base)
        num = num // base
    if len(_result) < size and size:
        [_result.insert(0, 0) for _ in range(size-len(_result))]
    return _result


def get_column(arr, idx, col) -> str:
    """
    Constructs column of 2D array.
    :param arr: 2D array
    :param idx: 1st index of 2D array
    :param col: Column to construct
    :return:
    """
    if col < 0:
        raise IndexError

    return "".join([bl[col] for bl in arr[idx]])


def find_differences(str1, str2) -> int:
    """
    Find number of differences between two strings
    :param str1: String 1
    :param str2: String 2
    :return:
    """
    if len(str1) != len(str2):
        raise IndexError

    return sum([1 if str1[d] != str2[d] else 0 for d in range(len(str1))])


def insert_column(arr, col, val):
    """
    Insert column into array
    :param arr:
    :param col:
    :param val:
    :return:
    """
    if 0 < len(arr.shape) < 3:
        # for 1d array
        for i in range(len(arr)):
            temp = str(arr[i])
            temp = temp[:col] + str(val) + temp[col+1:]
            arr[i] = temp
    else:
        raise "Array has too many dimensions"


def transpose(arr):
    """
    Returns the transpose (flip) of an array
    :param arr:
    :return:
    """
    return list(map("".join, zip(*arr)))


def rotate90a(arr):
    rows = len(arr)
    cols = len(arr[0])
    new_arr = []
    for c in range(cols-1, -1, -1):
        temp = ""
        for r in arr:
            temp += r[c]
        new_arr.append(temp)
    return new_arr


def rotate90c(arr):
    rows = len(arr)
    cols = len(arr[0])
    new_arr = []
    for c in range(cols):
        temp = ""
        for r in arr:
            temp = r[c] + temp
        new_arr.append(temp)
    return new_arr


def str_to_int(arr):
    """
    Converts list of strings to list of ints
    :param arr:
    :return:
    """
    if len(arr.asarray.shape) == 1:
        # 1d array
        return list(map(int, arr))
    elif len(arr.asarray.shape) == 2:
        # 2d array
        temp = []
        for i in range(len(arr)):
            temp.append(list(map(int, arr[i])))
        return temp
    else:
        raise "Array dimensions too large."


x, y = 0, 0
# up, down, left, right
for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    for distance in range(1, 4):
        nx = x + dx * distance
        ny = y + dy * distance


pos = namedtuple("pos", ["x", "y"])
node = namedtuple("node", ["val", "node", "last", "steps"])
def dijkstra(grid, start, end, min_moves=0, max_moves=0, showpath=True):
    """

    :param grid:
    :param start:
    :param end:
    :param min_moves:
    :param max_moves:
    :param showpath:
    :return:
    """
    def show_path(s, e):
        current = s
        path = [["." for _ in range(max_y)] for _ in range(max_x)]
        while current != e:
            path[current.x][current.y] = str(grid[current.x][current.y])
            current = closed_list[list(zip(*closed_list))[1].index(current)].last
        for r in path:
            print("".join(r))

    open_list = [node(0, pos(*start), pos(0, 0), 1)]
    closed_list = []
    max_x, max_y = len(grid), len(grid[0])
    max_moves = max_moves if max_moves else len(grid)
    min_moves = min_moves+1 if not min_moves else min_moves

    # loop until no more nodes left
    while open_list:
        # explore current node
        current_node = heappop(open_list)

        # searching is shortest first, so first time end point is found is the shortest path
        if current_node.node == pos(*end):
            closed_list.append(current_node)
            if showpath:
                show_path(pos(*end), pos(0, 0))
            return current_node.val

        # search is shortest first, so any node in closed list already has the shortest route to it
        if closed_list and current_node.node in list(zip(*closed_list))[1]:
            continue

        # add current node to closed list
        closed_list.append(current_node)

        # up, down, left, right
        # get neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            val = current_node.val
            for distance in range(min_moves, max_moves+1):
                nx = current_node.node.x + dx * distance
                ny = current_node.node.y + dy * distance

                last_pos = pos(current_node.node.x - dx, current_node.node.y - dy)

                # check if in range and not going backwards
                if -1 < nx < max_x and -1 < ny < max_y and tuple(np.subtract(current_node.node, current_node.last)) != (-dx, -dy):
                    val += grid[nx][ny]

                    # check if travelling in same direction and less then three steps in a row
                    if tuple(np.subtract(current_node.node, current_node.last)) == (dx, dy) and min_moves <= current_node.steps+distance < max_moves:
                        print("same direction")
                        print(node(val, pos(nx, ny), current_node.node, current_node.steps+1))
                        heappush(open_list, node(val, pos(nx, ny), last_pos, current_node.steps+distance))

                    # check if going either side (not in same direction)
                    if tuple(np.subtract(current_node.node, current_node.last)) != (dx, dy):
                        print("split direction")
                        print(node(val, pos(nx, ny), current_node.node, 1))
                        heappush(open_list, node(val, pos(nx, ny), last_pos, 1))


def find_possible_moves(data, grid, start, max_dist):
    """

    :param max_dist:
    :param data:
    :param grid:
    :param start:
    :return:
    """
    open_list = [node(0, pos(*start), pos(*start), "S")]
    closed_list = []
    max_x, max_y = len(grid), len(grid[0])

    # loop until no more nodes left
    while open_list:
        # explore current node
        current_node = heappop(open_list)

        if current_node.val > max_dist:
            continue

        # search is shortest first, so any node in closed list already has the shortest route to it
        if closed_list and current_node.node in list(zip(*closed_list))[1]:
            continue

        # add current node to closed list
        closed_list.append(current_node)

        # up, down, left, right
        # get neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = current_node.node.x + dx
            ny = current_node.node.y + dy

            # check if in range and not going backwards
            if -1 < nx < max_x and -1 < ny < max_y and tuple(np.subtract(current_node.node, current_node.last)) != (-dx, -dy):
                val = current_node.val + grid[nx][ny]
                heappush(open_list, node(val, pos(nx, ny), current_node.node, data[current_node.node.x][current_node.node.y]))

    total = 0
    for n in closed_list:
        if n.val <= max_dist and n.val % 2 == max_dist % 2 and n.type in [".", "S"]:
            total += 1
            data[n.node.x][n.node.y] = "O"
    return total


@functools.lru_cache(maxsize=None)
def t(): pass
