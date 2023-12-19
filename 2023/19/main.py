import re

data = [x for x in open("data2").read().strip().split("\n")]
proc = [x for x in open("data").read().strip().split("\n")]
slots = {}

for p in proc:
    label = p.split("{")[0]
    val = p.split("{")[1].split("}")[0]
    slots[label] = val

total = 0
for d in data:
    key = "in"
    x, m, a, s = [int(x) for x in re.findall(r"[\d]+", d)]

    while key != "A" and key != "R":
        instruc = slots[key].split(",")
        for i in instruc:
            if ":" in i:
                if eval(i.split(":")[0]):
                    key = i.split(":")[1]
                    break
            else:
                key = i
                break

        if key == "A":
            total += x + m + a + s

print(total)
