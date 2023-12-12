

with open("data.txt") as file:
    grid = file.readlines()
    path = [["."*140] for _ in range(140)]
    row = 25
    col = 77
    dir = "d"
    symbol = ""
    steps = 0

    while symbol != "S":
        # move
        if dir == "d":
            row += 1
        elif dir == "u":
            row -= 1
        elif dir == "r":
            col += 1
        else:
            col -= 1
        symbol = grid[row][col]
        steps += 1

        # get new direction
        if symbol == "F":
            if dir == "u":
                dir = "r"
            else:
                dir = "d"
        elif symbol == "7":
            if dir == "r":
                dir = "d"
            else:
                dir = "l"
        elif symbol == "L":
            if dir == "d":
                dir = "r"
            else:
                dir = "u"
        elif symbol == "J":
            if dir == "d":
                dir = "l"
            else:
                dir = "u"

    print(steps/2)
