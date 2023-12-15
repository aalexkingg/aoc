from helpers import transpose


def rotate90a(arr):
    rows = len(arr)
    cols = len(arr[0])
    new_arr = []
    for c in range(cols-1, -1, -1):
        temp = ""
        for r in arr:
            temp += r[c]
        new_arr.append(temp)
    return new_arr


def rotate90c(arr):
    rows = len(arr)
    cols = len(arr[0])
    new_arr = []
    for c in range(cols):
        temp = ""
        for r in arr:
            temp = r[c] + temp
        new_arr.append(temp)
    return new_arr


with open("data.txt") as f:
    lines = f.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n")

    grid = transpose(lines)
    copy_grid = []
    for j in range(40000000):
        if j % 4000 == 0:
            total = 0
            temp_grid = transpose(grid)
            print(temp_grid[0])
            for i in range(len(temp_grid)):
                total += (100 - i) * temp_grid[i].count("O")
            print(j / 4, total)

        for idx in range(len(grid[0])):
            for i in range(len(grid)):
                grid[i] = grid[i].replace(".O", "O.")

        grid = rotate90a(grid)






