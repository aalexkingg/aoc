
with open("data.txt") as file:
    lines = file.readlines()
    for i in range(140):
        lines[i] = lines[i].strip("\n")

    # insert rows
    for i in range(139, -1, -1):
        row = lines[i]
        if row.count("#") == 0:
            lines[i] = "X"*len(lines[i])

    # insert columns
    for i in range(139, -1, -1):
        col = ""
        for j in range(140):
            col += lines[j][i]

        if col.count("#") == 0:
            for j in range(140):
                temp = str(lines[j])
                temp = temp[:i] + "X" + temp[i+1:]
                lines[j] = temp

    # get positions of #'s
    positions = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "#":
                positions.append([i, j])

    # permutations of positions
    total = 0
    for i in range(len(positions)-1):
        for j in range(i+1, len(positions)):
            col1 = positions[j][1]
            col2 = positions[i][1]
            change_col = abs(col1 - col2)

            if col1 > col2:
                temp = lines[0][col2:col1]
            else:
                temp = lines[0][col1:col2]
            change_col += (temp.count("X") * 999999)

            row1 = positions[j][0]
            row2 = positions[i][0]
            change_row = abs(row1 - row2)

            num_x = 0
            if row1 > row2:
                for k in range(row2, row1):
                    if lines[k][0] == "X":
                        num_x += 1
            else:
                for k in range(row1, row2):
                    if lines[k][0] == "X":
                        num_x += 1
            change_row += (num_x * 999999)

            total += (change_row + change_col)

    print(total)
