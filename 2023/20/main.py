from collections import namedtuple

#node = namedtuple("node", ["type", "on", "pulse", "feed", "deps"])

data = [x for x in open("data").read().strip().split("\n")]

outputs = []
nodes = {}

for line in data:
    source, dest = line.split(" -> ")
    dest = dest.split(", ")
    nodes[source[1:]] = [source[0], 0, 0, dest, []]

for key, data in nodes.items():
    for f in data[3]:
        if f == "rx":
            continue
        if nodes[f][0] == "&":
            nodes[f][4].append(key)


high, low = 0, 0

for button in range(1,1000000000):
    q = [["roadcaster", 0]]
    while q:
        current, last_pulse = q[0]

        if current == "rx":


            if last_pulse == 0:
                print("button", button)
            q.pop(0)
            continue

        typ, on, pulse, feed, deps = nodes[current]

        if typ == "b":
            low += 1
            for f in feed:
                q.append([f, 0])
                low += 1

        elif typ == "%":
            if last_pulse == 0:
                nodes[current][1] = 1 - on
                if nodes[current][1] == 1:
                    last_pulse = 1
                else:
                    last_pulse = 0

                for f in feed:
                    q.append([f, last_pulse])
                    if last_pulse == 1:
                        high += 1
                    else:
                        low += 1
                nodes[current][2] = last_pulse

        else:
            for d in deps:
                if nodes[d][2] == 0:
                    last_pulse = 1
                    break
            else:
                last_pulse = 0

            for f in feed:
                q.append([f, last_pulse])
                if last_pulse == 1:
                    high += 1
                else:
                    low += 1

            nodes[current][2] = last_pulse

            if current in ["xj", "qs", "kz", "km"] and last_pulse == 1:
                print(current, last_pulse, button)
        q.pop(0)

print(low, high)
print(low * high)
