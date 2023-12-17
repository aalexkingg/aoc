from collections import namedtuple

pos = namedtuple("pos", ["x", "y"])
node = namedtuple("node", ["flag", "node", "last", "val", "route"])


#t = [["a", "bb"], ["c", "dd"], ["e", "ff"]]
#print(list(zip(*t)))
#print(list(enumerate(list(zip(*t))[0])))
#print(list(zip(*t))[0].index("c"))
#x = t[0]
#x[0] = "aa"
#print(t)
#print(x)
#exit()


def A_star(arr, start, end):
    open_list = [node(0, pos(*start), pos(-1, 0), 0, "   ")]
    path = [["." for _ in range(141)] for _ in range(141)]

    # current_low_cost = min(current_low_cost, parent_cost)
    # sorted(cards, key=lambda x: (x[0],x[1]))
    # explore, gets all nodes connected and adds them to open list,
    #  adds current node to closed list if its value is less than existing node

    # open list needs to be stored in order of lowest cost
    i = 0
    # loop until no more nodes left
    while min(open_list)[0] == 0:
        # explore current node
        current_node = sorted(open_list, key=lambda x: (x.flag, x.val))[0]

        # get connected nodes in other three directions and add to open list with costs
        # create up
        nx = current_node.node.x-1
        ny = current_node.node.y
        nroute = (current_node.route+"u")[-3:]
        if (nx, ny) != current_node.last and -1 < nx < 141 and -1 < ny < 141 and current_node.route != "uuu":
            val = current_node.val + grid[nx][ny]
            if (nx, ny) in list(zip(*open_list))[1]:
                idx = list(zip(*open_list))[1].index((nx, ny))
                if open_list[idx].val > val:
                    open_list[idx] = node(0, pos(nx, ny), current_node.node, val, nroute)
                elif (open_list[idx].val == val and
                      (nroute[-1] == "u" and (open_list[idx].route[-2:] == "uu" or open_list[idx].route == "uuu") or
                        nroute[-2:] == "uu" and open_list[idx].route == "uuu")):
                    open_list[idx] = node(0, pos(nx, ny), current_node.node, val, nroute)
            else:
                open_list.append(node(0, pos(nx, ny), current_node.node, val, nroute))

        # create down
        nx = current_node.node.x+1
        ny = current_node.node.y
        nroute = (current_node.route+"d")[-3:]
        if (nx, ny) != current_node.last and -1 < nx < 141 and -1 < ny < 141 and current_node.route != "ddd":
            val = current_node.val + grid[nx][ny]
            if (nx, ny) in list(zip(*open_list))[1]:
                idx = list(zip(*open_list))[1].index((nx, ny))
                if open_list[idx].val > val:
                    open_list[idx] = node(0, pos(nx, ny), current_node.node, val, nroute)
                elif (open_list[idx].val == val and
                      (nroute[-1] == "d" and (open_list[idx].route[-2:] == "dd" or open_list[idx].route == "ddd") or
                       nroute[-2:] == "dd" and open_list[idx].route == "ddd")):
                    open_list[idx] = node(0, pos(nx, ny), current_node.node, val, nroute)
            else:
                open_list.append(node(0, pos(nx, ny), current_node.node, val, nroute))

        # create left
        nx = current_node.node.x
        ny = current_node.node.y-1
        nroute = (current_node.route+"l")[-3:]
        if (nx, ny) != current_node.last and -1 < nx < 141 and -1 < ny < 141 and current_node.route != "lll":
            val = current_node.val + grid[nx][ny]
            if (nx, ny) in list(zip(*open_list))[1]:
                idx = list(zip(*open_list))[1].index((nx, ny))
                if open_list[idx].val > val:
                    open_list[idx] = node(0, pos(nx, ny), current_node.node, val, nroute)
                elif (open_list[idx].val == val and
                      (nroute[-1] == "l" and (open_list[idx].route[-2:] == "ll" or open_list[idx].route == "lll") or
                       nroute[-2:] == "ll" and open_list[idx].route == "lll")):
                    open_list[idx] = node(0, pos(nx, ny), current_node.node, val, nroute)
            else:
                open_list.append(node(0, pos(nx, ny), current_node.node, val, nroute))

        # create right
        nx = current_node.node.x
        ny = current_node.node.y+1
        nroute = (current_node.route+"r")[-3:]
        if (nx, ny) != current_node.last and -1 < nx < 141 and -1 < ny < 141 and current_node.route != "rrr":
            val = current_node.val + grid[nx][ny]
            if (nx, ny) in list(zip(*open_list))[1]:
                idx = list(zip(*open_list))[1].index((nx, ny))
                if open_list[idx].val > val:
                    open_list[idx] = node(0, pos(nx, ny), current_node.node, val, nroute)
                elif (open_list[idx].val == val and
                      (nroute[-1] == "r" and (open_list[idx].route[-2:] == "rr" or open_list[idx].route == "rrr") or
                       nroute[-2:] == "rr" and open_list[idx].route == "rrr")):
                    open_list[idx] = node(0, pos(nx, ny), current_node.node, val, nroute)
            else:
                open_list.append(node(0, pos(nx, ny), current_node.node, val, nroute))

        # add current node to closed list
        open_list[open_list.index(current_node)] = node(1, current_node.node, current_node.last, current_node.val, current_node.route)

        print(len(open_list), list(zip(*open_list))[0].count(0))

    print(open_list[list(zip(*open_list))[1].index((140, 140))])
    current = pos(140, 140)
    total = 0
    while current != (-1, 0):
        total += grid[current.x][current.y]
        path[current.x][current.y] = str(grid[current.x][current.y])
        current = open_list[list(zip(*open_list))[1].index(current)].last

    print(total-grid[0][0])

    for r in path:
        print("".join(r))

    return open_list[list(zip(*open_list))[1].index((end[0]-1, end[1]-1))].val


with open("data") as f:
    # weighted graph
    # A* algorithm
    grid = list(map(lambda x: x.strip("\n"), f.readlines()))
    temp = []
    for i in range(len(grid)):
        temp.append(list(map(int, grid[i])))
    grid = temp

    shortest = A_star(grid, (0, 0), (141, 141))

    print(shortest)
