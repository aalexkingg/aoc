
def move(x, y, dir):
    while True:
        if x < 0 or x > 109 or y < 0 or y > 109:
            break

        if visited[x][y] > 19:
            print("exceed")
            break


        # add pos to pos array
        visited[x][y] += 1

        if dir in "rl" and grid[x][y] in ".-":
            # increment pos
            if dir == "r":
                y += 1
            else:
                y -= 1

        elif dir in "ud" and grid[x][y] in ".|":
            # increment pos
            if dir == "u":
                x -= 1
            else:
                x += 1

        elif grid[x][y] == "\\":
            # change dir
            # increment pos
            if dir == "r":
                dir = "d"
                x += 1
            elif dir == "l":
                dir = "u"
                x -= 1
            elif dir == "d":
                dir = "r"
                y += 1
            else:
                dir = "l"
                y -= 1

        elif grid[x][y] == "/":
            # change dir
            # increment pos
            if dir == "l":
                dir = "d"
                x += 1
            elif dir == "r":
                dir = "u"
                x -= 1
            elif dir == "u":
                dir = "r"
                y += 1
            else:
                dir = "l"
                y -= 1

        elif dir in "rl" and grid[x][y] == "|":
            if visited[x][y] > 1:
                break

            # recurse
            move(x-1, y, "u")

            dir = "d"
            x += 1

        elif dir in "ud" and grid[x][y] == "-":
            if visited[x][y] > 1:
                break

            # recurse
            move(x, y-1, "l")

            dir = "r"
            y += 1


def calc_total():
    tot = 0
    # sum visited for not 0
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            tot += 1 if visited[i][j] > 0 else 0
    return tot


with open("data") as f:
    grid = f.readlines()
    grid = [g.strip("\n") for g in grid]

    # part 1
    visited = [[0 for _ in range(len(grid))] for _ in range(len(grid[0]))]
    move(0, 0, "r")
    total = calc_total()
    print(total)

    # part 2
    max_total = 0
    for a in range(110):
        visited = [[0 for _ in range(len(grid))] for _ in range(len(grid[0]))]
        move(a, 0, "r")
        total = calc_total()
        max_total = max(total, max_total)

        visited = [[0 for _ in range(len(grid))] for _ in range(len(grid[0]))]
        move(a, 109, "l")
        total = calc_total()
        max_total = max(total, max_total)

        visited = [[0 for _ in range(len(grid))] for _ in range(len(grid[0]))]
        move(0, a, "d")
        total = calc_total()
        max_total = max(total, max_total)

        visited = [[0 for _ in range(len(grid))] for _ in range(len(grid[0]))]
        move(109, a, "u")
        total = calc_total()
        max_total = max(total, max_total)

    print(max_total)
