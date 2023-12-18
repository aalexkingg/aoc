data = [x.split(" ") for x in open("data").read().strip().split("\n")]
grid = [["." for _ in range(382)] for _ in range(422)]
#grid = [["." for _ in range(7)] for _ in range(10)]
x, y = 233, 0
for i in data:
    print(x, y, i[0], i[1])
    if i[0] == "U":
        for j in range(int(i[1])):
            grid[x-1-j][y] = "#"
        x -= int(i[1])

    elif i[0] == "D":
        for j in range(int(i[1])):
            grid[x+1+j][y] = "#"
        x += int(i[1])

    elif i[0] == "R":
        for j in range(int(i[1])):
            grid[x][y+1+j] = "#"
        y += int(i[1])

    else:
        for j in range(int(i[1])):
            grid[x][y-1-j] = "#"
        y -= int(i[1])

if True:
    total = 0
    for i, r in enumerate(grid):
        row = "".join(r)

        #last = row.rfind('#')
        #for i in range(last+1, len(row)):
        #    row[i] = ","

        inout = 0
        updown = ""
        for col in range(len(row)-1):
            if row[col] == "#" and row[col-1] == "." and row[col+1] == "#":
                if grid[i+1][col] == "#":
                    updown = "d"
                else:
                    updown = "u"

            if row[col-1] == "#" and row[col] == "#" and row[col+1] == ".":
                if (grid[i+1][col] == "#" and updown == "u") or (grid[i+1][col] == "." and updown == "d"):
                    inout = 1 - inout

            if row[col] == "#" and row[col+1] == "." and row[col-1] == ".":
                inout = 1 - inout
            if row[col] == "." and inout == 1:
                r[col] = "#"
                #pass

        total += r.count("#")
        print(total)

for d in grid:
    print("".join(d))




