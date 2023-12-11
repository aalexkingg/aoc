

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
        print(row, col)
        temp = str(path[row])
        temp = temp[:col] + symbol + temp[col+1:]
        path[row] = temp
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

    temp = str(path[25])
    temp = temp[:77] + "|" + temp[78:]
    path[25] = temp


    count = 0
    for i in range(140):
        inout = "O"
        up = 0
        down = 0
        temp = str(path[i])
        for j in range(140):

            if temp[j] == ".":
                temp = temp[:j] + inout + temp[j+1:]
            elif temp[j] == "-":
                pass
            elif temp[j] == "|":
                up = 1
                down = 1
            elif temp[j] == "F" or temp[j] == "7":
                down = 1 - down
            elif temp[j] == "L" or temp[j] == "J":
                up = 1 - up

            if up == 1 and down == 1:
                inout = "I" if inout == "O" else "O"
                up = 0
                down = 0

        path[i] = temp
        count += temp.count("I")

    print(steps / 2)
    for i in range(140):
        print(path[i])

    print(count)



