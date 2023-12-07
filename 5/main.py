import re
import numpy as np

map = np.empty([7, 41, 3])

with open("data.txt") as file:
    lines = file.readlines()

    seeds = re.findall(r"[\d][\d]+", lines[0])


    #exit()

    for s in range(len(seeds)):
        seeds[s] = int(seeds[s])



    for i in range(3, 35):
        data = re.findall(r"[\d]+", lines[i])
        map[6][i-3][0] = int(data[0])
        map[6][i-3][1] = int(data[1])
        map[6][i-3][2] = int(data[2])

    for i in range(37, 72):
        data = re.findall(r"[\d]+", lines[i])
        map[5][i - 37][0] = int(data[0])
        map[5][i - 37][1] = int(data[1])
        map[5][i - 37][2] = int(data[2])

    for i in range(74, 101):
        data = re.findall(r"[\d]+", lines[i])
        map[4][i-74][0] = int(data[0])
        map[4][i-74][1] = int(data[1])
        map[4][i-74][2] = int(data[2])

    for i in range(103, 120):
        data = re.findall(r"[\d]+", lines[i])
        map[3][i-103][0] = int(data[0])
        map[3][i-103][1] = int(data[1])
        map[3][i-103][2] = int(data[2])

    for i in range(123, 164):
        data = re.findall(r"[\d]+", lines[i])
        map[2][i-123][0] = int(data[0])
        map[2][i-123][1] = int(data[1])
        map[2][i-123][2] = int(data[2])

    for i in range(166, 203):
        data = re.findall(r"[\d]+", lines[i])
        map[1][i-166][0] = int(data[0])
        map[1][i-166][1] = int(data[1])
        map[1][i-166][2] = int(data[2])

    for i in range(205, 244):
        data = re.findall(r"[\d]+", lines[i])
        map[0][i-205][0] = int(data[0])
        map[0][i-205][1] = int(data[1])
        map[0][i-205][2] = int(data[2])

    min_value = 999999999999999

    for i in range(5200000, 5202000):
    #print(seeds[i],seeds[i+1])
        old_value = i
        #print(i)
        #print("Seed ", old_value)
        for block in range(7):
            for item in range(len(map[block])):
                if map[block][item][0] <= old_value < map[block][item][0] + map[block][item][2]:
                    old_value = map[block][item][1] + old_value - map[block][item][0]
                    #print(old_value)
                    break
        print(i, old_value)
        for j in range(len(seeds[::2])):
            if seeds[j] <= old_value < seeds[j]+seeds[j+1]:
                print("Old val", i)
                exit()
