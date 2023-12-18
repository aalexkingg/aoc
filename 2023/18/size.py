data = [x.split(" ") for x in open("data").read().strip().split("\n")]

minx, miny = 0, 0
maxx, maxy = 0, 0

minval = 0


dirs = ["R", "D", "L", "U"]

x, y = 0, 0
for i in data:
    temp = i[2].strip("(#)")
    dir = dirs[int(temp[-1])]
    num = int(temp[:-1], 16)
    minval = max(num, minval)
    if dir == "U":
        x -= num
        minx = min(x, minx)
    elif dir == "D":
        x += num
        maxx = max(x, maxx)
    elif dir == "R":
        y += num
        maxy = max(y, maxy)
    else:
        y -= num
        miny = min(y, miny)

print(minx, miny, maxx, maxy)
print(minval)




