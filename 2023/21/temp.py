from collections import namedtuple
import numpy as np
from heapq import heappop, heappush
from math import floor

pos = namedtuple("pos", ["x", "y"])
node = namedtuple("node", ["val", "node", "last", "type"])


def find_possible_moves(grid, start, max_dist):
    """

    :param grid:
    :param start:
    :param end:
    :param min_moves:
    :param max_moves:
    :param showpath:
    :return:
    """
    open_list = [node(0, pos(*start), pos(*start), data[start[0]][start[1]])]
    closed_list = []
    max_x, max_y = len(grid), len(grid[0])

    # loop until no more nodes left
    while open_list:
        # explore current node
        current_node = heappop(open_list)

        if current_node.val > max_steps:
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

    for da in data:
        print("".join(da))

    print(total)
    return total


data = [[y for y in x] for x in open("data").read().strip().split("\n")]
S = pos(floor(len(data[0]) / 2), floor(len(data[0]) / 2))

max_steps = 130
odd = 7407
even = 7481
# hashes = 2267

g = [[1 for y in range(len(data[x]))] for x in range(len(data))]
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "#":
            g[i][j] = 9999

max_steps = 64
total = 0
for x, y in [(0, 0), (130, 0), (130, 130), (0, 130)]:
    total += find_possible_moves(g, pos(x, y), max_steps)
print("sides", total)

max_steps = 130
#num_1 = find_possible_moves(g, pos(0, 65), max_steps)
#num_2 = find_possible_moves(g, pos(65, 0), max_steps)

total = 0
for d in data:
    total += "".join(d).count("O")
print(total)

max_steps = 26501365
n_max_steps = max_steps - 65
grids = n_max_steps / 131

odds = 202299**2
evens = 202300**2
print(odds)

odd_total = odds * odd
even_total = evens * even
print(odd_total, even_total)

edges = 202299 * 25973 + total * 202300
corners = 22318

total = odd_total + even_total + edges + corners
print(total)

