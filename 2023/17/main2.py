from collections import namedtuple
import numpy as np
from heapq import heappop, heappush


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
    pos = namedtuple("pos", ["x", "y"])
    node = namedtuple("node", ["val", "node", "last", "steps"])

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


arr = [[int(y) for y in x] for x in open("inp").read().strip().split("\n")]
shortest = dijkstra(arr, (0, 0), (12, 12), max_moves=3)
print(shortest)
