from collections import namedtuple

pos = namedtuple("pos", ["x", "y"])
node = namedtuple("node", ["flag", "node", "last", "val", "route"])

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
    open_list = [node(0, pos(*start), pos(-1, 0), 0, " ")]
    max_x, max_y = len(grid), len(grid[0])
    path = [["." for _ in range(max_y)] for _ in range(max_x)]

    # current_low_cost = min(current_low_cost, parent_cost)
    # sorted(cards, key=lambda x: (x[0],x[1]))
    # explore, gets all nodes connected and adds them to open list,
    #  adds current node to closed list if its value is less than existing node

    # open list needs to be stored in order of lowest cost

    # loop until no more nodes left
    while min(open_list)[0] == 0:
        # explore current node
        current_node = sorted(open_list, key=lambda x: (x.flag, x.val))[0]
        if current_node.route != "l" and current_node.route != "r":
            vall = current_node.val
            valr = current_node.val
            # create up/down
            for i in range(1, 4):
                nx = current_node.node.x
                ny = current_node.node.y - i
                nroute = "l"
                if (nx, ny) != current_node.last and -1 < nx < max_x and -1 < ny < max_y:
                    vall += grid[nx][ny]
                    if (nx, ny) in list(zip(*open_list))[1]:
                        idx = list(zip(*open_list))[1].index((nx, ny))
                        if open_list[idx].val >= vall:
                            open_list[idx] = node(0, pos(nx, ny), pos(nx, ny+1), vall, nroute)
                        elif open_list[idx].val > vall:
                            open_list.append(node(0, pos(nx, ny), pos(nx, ny+1), vall, nroute))
                    else:
                        open_list.append(node(0, pos(nx, ny), pos(nx, ny+1), vall, nroute))

                nx = current_node.node.x
                ny = current_node.node.y + i
                nroute = "r"
                if (nx, ny) != current_node.last and -1 < nx < max_x and -1 < ny < max_y:
                    valr += grid[nx][ny]
                    if (nx, ny) in list(zip(*open_list))[1]:
                        idx = list(zip(*open_list))[1].index((nx, ny))
                        if open_list[idx].val >= valr:
                            open_list[idx] = node(0, pos(nx, ny), pos(nx, ny-1), valr, nroute)
                        elif open_list[idx].val > valr:
                            open_list.append(node(0, pos(nx, ny), pos(nx, ny-1), valr, nroute))
                    else:
                        open_list.append(node(0, pos(nx, ny), pos(nx, ny-1), valr, nroute))
        if current_node.route != "u" and current_node.route != "d":
            valu = current_node.val
            vald = current_node.val
            # create up/down
            for i in range(1, 4):
                nx = current_node.node.x - i
                ny = current_node.node.y
                nroute = "u"
                if (nx, ny) != current_node.last and -1 < nx < max_x and -1 < ny < max_y:
                    valu += grid[nx][ny]
                    if (nx, ny) in list(zip(*open_list))[1]:
                        idx = list(zip(*open_list))[1].index((nx, ny))
                        if open_list[idx].val >= valu:
                            open_list[idx] = node(0, pos(nx, ny), pos(nx+1, ny), valu, nroute)
                        elif open_list[idx].val > valu:
                            open_list.append(node(0, pos(nx, ny), pos(nx+1, ny), valu, nroute))
                    else:
                        open_list.append(node(0, pos(nx, ny), pos(nx+1, ny), valu, nroute))

                nx = current_node.node.x + i
                ny = current_node.node.y
                nroute = "d"
                if (nx, ny) != current_node.last and -1 < nx < max_x and -1 < ny < max_y:
                    vald += grid[nx][ny]
                    if (nx, ny) in list(zip(*open_list))[1]:
                        idx = list(zip(*open_list))[1].index((nx, ny))
                        if open_list[idx].val >= vald:
                            open_list[idx] = node(0, pos(nx, ny), pos(nx-1, ny), vald, nroute)
                        elif open_list[idx].val > valu:
                            open_list.append(node(0, pos(nx, ny), pos(nx-1, ny), vald, nroute))
                    else:
                        open_list.append(node(0, pos(nx, ny), pos(nx-1, ny), vald, nroute))

        # add current node to closed list
        open_list[open_list.index(current_node)] = node(1, current_node.node, current_node.last, current_node.val, current_node.route)

        print(len(open_list), list(zip(*open_list))[0].count(0))


    print(open_list[list(zip(*open_list))[1].index((end[0], end[1]))])
    current = pos(end[0], end[1])
    total = 0
    while current != (-1, 0):
        total += grid[current.x][current.y]
        path[current.x][current.y] = str(grid[current.x][current.y])
        current = open_list[list(zip(*open_list))[1].index(current)].last

    print(total-grid[start[0]][start[1]])

    for r in path:
        print("".join(r))

    return open_list[list(zip(*open_list))[1].index((end[0]-1, end[1]-1))].val


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
