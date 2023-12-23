data = [x for x in open("data").read().strip().split("\n")]

blocks = []

for line in data:
    temp = line.split("~")
    blocks.append([[int(y) for y in temp[0].split(",")], [int(y) for y in temp[1].split(",")]])

tower = [[[0 for x in range(10)] for y in range(10)] for z in range(257)]

for num, block in enumerate(blocks):
    num += 1
    for x in range(block[0][0], block[1][0]+1):
        for y in range(block[0][1], block[1][1]+1):
            for z in range(block[0][2], block[1][2]+1):
                tower[z][y][x] = num

swaps = True
while swaps:
    swaps = False
    moved = []
    for z in range(2, 257):
        for y in range(10):
            for x in range(10):
                if tower[z][y][x] != 0 and tower[z][y][x] not in moved:
                    # find others
                    temp_pos = []
                    temp_pos.append((y, x))
                    if x < 9:
                        for i in range(x+1, 10):
                            if tower[z][y][i] == tower[z][y][x]:
                                temp_pos.append((y, i))
                    if y < 9:
                        for j in range(y+1, 10):
                            if tower[z][j][x] == tower[z][y][x]:
                                temp_pos.append((j, x))

                    if len(temp_pos) > 1:
                        moved.append(tower[z][y][x])

                    # check row below
                    total = 0
                    for item in temp_pos:
                        total += tower[z-1][item[0]][item[1]]

                    # move
                    if total == 0:
                        swaps = True
                        for item in temp_pos:
                            tower[z - 1][item[0]][item[1]] = tower[z][item[0]][item[1]]
                            tower[z][item[0]][item[1]] = 0

                    del temp_pos
    del moved

max_layer = 0
for z in range(1, 257):
    if sum(sum(tower[z], [])) == 0:
        max_layer = z
        break

blockers = []
found = []
for z in range(max_layer-1, 1, -1):
    for y in range(10):
        for x in range(10):
            if tower[z][y][x] != 0 and tower[z][y][x] not in found:
                # find others
                temp_pos = []
                temp_pos.append((y, x))
                if x < 9:
                    for i in range(x + 1, 10):
                        if tower[z][y][i] == tower[z][y][x]:
                            temp_pos.append((y, i))
                if y < 9:
                    for j in range(y + 1, 10):
                        if tower[z][j][x] == tower[z][y][x]:
                            temp_pos.append((j, x))

                if len(temp_pos) > 1:
                    found.append(tower[z][y][x])

                below = {}
                for item in temp_pos:
                    if tower[z-1][item[0]][item[1]] != 0:
                        below[tower[z-1][item[0]][item[1]]] = 1

                if len(below) == 1:
                    blockers.append(tower[z][y][x])
                del below

total = 0
found = []
for z in range(1, max_layer):
    for y in range(10):
        for x in range(10):
            if tower[z][y][x] != 0 and tower[z][y][x] not in found:
                # find others
                temp_pos = []
                temp_pos.append((y, x))
                if x < 9:
                    for i in range(x + 1, 10):
                        if tower[z][y][i] == tower[z][y][x]:
                            temp_pos.append((y, i))
                if y < 9:
                    for j in range(y + 1, 10):
                        if tower[z][j][x] == tower[z][y][x]:
                            temp_pos.append((j, x))

                if len(temp_pos) > 1:
                    found.append(tower[z][y][x])

                for item in temp_pos:
                    if tower[z+1][item[0]][item[1]] in blockers:
                        break
                else:
                    total += 1

print(len(set(blockers)))
print(total)
"""
total = 0
moved = []
for z in range(1, max_layer):
    for y in range(10):
        for x in range(10):
            if tower[z][y][x] != 0 and tower[z][y][x] not in moved:
                temp_pos = []
                temp_pos.append((y, x))
                if x < 9:
                    for i in range(x + 1, 10):
                        if tower[z][y][i] == tower[z][y][x]:
                            temp_pos.append((y, i))
                if y < 9:
                    for j in range(y + 1, 10):
                        if tower[z][j][x] == tower[z][y][x]:
                            temp_pos.append((j, x))

                if len(temp_pos) > 1:
                    moved.append(tower[z][y][x])
                    
                above = {}
                for item in temp_pos:
                    if tower[z+1][item[0]][item[1]] != 0 and tower[z+1][item[0]][item[1]] != tower[z][y][x]:
                        if 
                        above.append([tower[z+1][item[0]][item[1]], ])
                    
                for item in above:
       

for z in range(len(tower)):
    print(z)
    for y in range(len(tower[z])):
        print(tower[z][y])
"""