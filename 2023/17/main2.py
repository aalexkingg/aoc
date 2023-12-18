from collections import namedtuple
import numpy as np


pos = namedtuple("pos", ["x", "y"])
node = namedtuple("node", ["node", "last", "val", "steps"])

#grid = [[int(y) for y in x] for x in open("data").read().strip().split("\n")]

#t = [["a", "bb"], ["c", "dd"], ["e", "ff"]]
#print(list(zip(*t)))
#print(list(enumerate(list(zip(*t))[0])))
#print(list(zip(*t))[0].index("c"))
#x = t[0]
#x[0] = "aa"
#print(t)
#print(x)
#exit()



def A_star(grid, start, end):
    open_list = [node(pos(*start), pos(-1, 0), 0, 0)]
    closed_list = []
    max_x, max_y = len(grid), len(grid[0])

    # loop until no more nodes left
    while open_list:
        # explore current node
        open_list = sorted(open_list, key=lambda x: x.val)
        current_node = open_list[0]

        # searching is shortest first, so first time end point is found is the shortest path
        if current_node.node == end:
            print("End")
            current = pos(*end)
            path = [["." for _ in range(max_y)] for _ in range(max_x)]
            while current != (-1, 0):
                path[current.x][current.y] = str(grid[current.x][current.y])
                current = closed_list[list(zip(*closed_list))[0].index(current)].last

            for r in path:
                print("".join(r))
            return current_node.val

        # search is shortest first, so any node in closed list already has shortest route to it
        if current_node in closed_list:
            continue

        # add current node to closed list
        closed_list.append(current_node)
        open_list.pop(0)

        # up, down, left, right
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for direction in range(4):
            # check for 3 moves limit

            nx = current_node.node.x + dirs[direction][0]
            ny = current_node.node.y + dirs[direction][1]
            if (nx, ny) != current_node.last and -1 < nx < max_x and -1 < ny < max_y:
                if current_node.steps < 3 and direction == (current_node.node.x - current_node.last.x, current_node.node.y - current_node.last.y):
                    # add in same direction
                    open_list.append(node(pos(nx, ny), current_node.node, current_node.val + grid[nx][ny], current_node.steps+1))
                elif direction != (current_node.node.x - current_node.last.x, current_node.node.y - current_node.last.y):
                    # and not in same direction
                    open_list.append(node(pos(nx, ny), current_node.node, current_node.val + grid[nx][ny],  1))

        print(len(open_list), len(closed_list))


with open("inp") as f:
    # weighted graph
    # A* algorithm
    arr = list(map(lambda x: x.strip("\n"), f.readlines()))
    temp = []
    for i in range(len(arr)):
        temp.append(list(map(int, arr[i])))
    arr = temp

    shortest = A_star(arr, (0, 0), (12, 12))

    print(shortest)
