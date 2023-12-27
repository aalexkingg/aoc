data = [x for x in open("data").read().strip().split("\n")]

comps = {}
deads = []

for d in data:
    label = d.split(": ")[0]
    values = d.split(": ")[1].split(" ")
    comps[label] = values

for d in data:
    label = d.split(": ")[0]
    values = d.split(": ")[1].split(" ")
    for val in values:
        try:
            comps[val].append(label)
        except KeyError:
            comps[val] = [label]
            deads.append(val)


list1 = ["qsf", "vvz"]
list2 = ["dzt", "bbf"]
unallocated = list(comps.keys())
for l1, l2 in zip(list1, list2):
    unallocated.remove(l1)
    unallocated.remove(l2)

while len(unallocated) > 0:
    for current in unallocated.copy():
        score1 = 0
        score2 = 0
        for cons in comps[current]:
            if cons in list1:
                score1 += 1
            elif cons in list2:
                score2 += 1

        if score1 > score2:
            list1.append(current)
            unallocated.remove(current)
        elif score2 > score1:
            list2.append(current)
            unallocated.remove(current)

        if score1 > 0 and score2 > 0:
            print(current, score1, score2)

    print(len(list1), len(list2), len(unallocated))


