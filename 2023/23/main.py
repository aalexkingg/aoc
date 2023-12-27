
def path(pos, direction, moves, nodes):
    while True:
        if direction == "u":
            xx, yy = -1, 0
        elif direction == "d":
            xx, yy = 1, 0
        elif direction == "l":
            xx, yy = 0, -1
        else:
            xx, yy = 0, 1

        try:
            while data[pos[0]+xx][pos[1]+yy] == ".":
                moves += 1
                pos = (pos[0]+xx, pos[1]+yy)

                #print(pos)
        except IndexError:
            print(moves)
            global max_moves
            max_moves = max(max_moves, moves)
            return

        if data[pos[0]+xx][pos[1]+yy] == "#":
            # change direction
            if direction == "l" or direction == "r":
                if data[pos[0]-1][pos[1]] == "#":
                    direction = "d"
                else:
                    direction = "u"
            else:
                if data[pos[0]][pos[1]-1] == "#":
                    direction = "r"
                else:
                    direction = "l"
        else:
            # arrow
            moves += 2
            #print(moves, pos, xx, yy)
            pos = (pos[0] + 2*xx, pos[1] + 2*yy)
            if pos not in nodes:
                print(pos)
                nodes.append(pos)
                # find 2 routes
                if data[pos[0]+1][pos[1]] == "v" and direction != "u":
                    print(direction, "d")
                    path((pos[0]+2, pos[1]), "d", moves+2, nodes)
                if data[pos[0]][pos[1]+1] == ">" and direction != "l":
                    print(direction, "r")
                    path((pos[0], pos[1]+2), "r", moves+2, nodes)
                if data[pos[0]][pos[1]+1] == ">" and direction != "r":
                    print(direction, "l")
                    path((pos[0], pos[1]-2), "l", moves+2, nodes)
                if data[pos[0]+1][pos[1]] == "v" and direction != "d":
                    print(direction, "u")
                    path((pos[0]-2, pos[1]), "u", moves+2, nodes)

            return


data = [x for x in open("test").read().strip().split("\n")]
pos = (0, 1)
direction = "d"
#nodes = []
max_moves = 0
path(pos, direction, 0, [])
print(max_moves)

