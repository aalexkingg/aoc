

with open("data.txt") as file:
    lines = file.readlines()

    # insert columns
    for i in range(139, -1, -1):
        col = ""
        for j in range(140):
            col += lines[j][i]

        if col.count("#") == 0:
            for j in range(140):
                temp = str(lines[j])
                temp = temp[:i] + "." + temp[i:]
                lines[j] = temp

    # insert rows
    for i in range(139, -1, -1):
        row = lines[i]
        if row.count("#") == 0:
            lines.insert(i, row)

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
            total += abs(positions[j][0] - positions[i][0]) + abs(positions[j][1] - positions[i][1])

    print(total)
