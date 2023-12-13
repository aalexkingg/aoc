from functools import reduce

with open("data.txt") as f:
    most = [0, 0, 0]
    current = 0
    for l in f:
        if l.strip("\n") == "":
            for i in range(3):
                if current > most[i]:
                    most[i] = current
                    break

            current = 0
        else:
            current += int(l)

    print(sum(most))

