from math import *
file = "data"
max_steps = 64

#file = "test"
#max_steps = 6


data = [x for x in open(file).read().strip().split("\n")]
S = (floor(len(data[0])/2), floor(len(data[0])/2))

total = 0
for row in data:
    total += row.count("#")
print(total)
exit()
# remove spaces too far away from center
for i, row in enumerate(data):
    for j, char in enumerate(row):
        dist = abs(i - S[0]) + abs(j - S[1])
        if dist > max_steps:
            if data[i][j] == ".":
                data[i][j] = "A"

# find valid positions
# if distance divisible by 2, and in range, then valid
for i, row in enumerate(data):
    for j, char in enumerate(row):
        if data[i][j] in ["#", "S", "A"]:
            continue

        dist = abs(i - S[0]) + abs(j - S[1])
        if dist % 2 == 0:
            data[i][j] = "X"

total = 0
for row in data:
    total += row.count("X")

print(total)

for d in data:
    print("".join(d))
