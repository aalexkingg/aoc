data = [x.split(" ") for x in open("data").read().strip().split("\n")]
grid = [[] for _ in range(15083010)]

x, y = 4262950, 0
dirs = ["R", "D", "L", "U"]

for i, d in enumerate(data):
    temp = d[2].strip("(#)")
    dir = dirs[int(temp[-1])]
    num = int(temp[:-1], 16)

    if dir == "U":
        for row in range(x-1, x-num, -1):
            # populate
            grid[row].append((y, y, 1))
        x -= int(num)

    elif dir == "D":
        for row in range(x+1, x+num):
            # populate
            grid[row].append((y, y, 1))
        x += int(num)

    elif dir == "R":
        start = y
        end = y + num
        # barrier
        barrier = 0
        if 0 < i < len(data)-1:
            if data[i-1][2][-2] == data[i+1][2][-2]:
                barrier = 1
        # populate
        grid[x].append((start, end, barrier))
        y += int(num)

    else:
        start = y - num
        end = y
        # barrier
        barrier = 0
        if 0 < i < len(data)-1:
            if data[i-1][2][-2] == data[i+1][2][-2]:
                barrier = 1
        # populate
        grid[x].append((start, end, barrier))
        y -= int(num)

total = 0
for z, row in enumerate(grid):
    rows = sorted(row)

    outin = 0
    for i, r in enumerate(rows):
        total += r[1] - r[0] + 1

        if r[2] == 1:
            outin = 1 - outin

        total += (rows[i+1][0] - r[1] - 1) * outin

print(total)


