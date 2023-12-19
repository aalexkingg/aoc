proc = [x for x in open("data").read().strip().split("\n")]
slots = {}

for p in proc:
    label = p.split("{")[0]
    val = p.split("{")[1].split("}")[0]
    slots[label] = val


def tree(key, x, m, a, s):
    xcopy, mcopy, acopy, scopy = x.copy(), m.copy(), a.copy(), s.copy()
    for c in slots[key].split(","):
        print(c)
        xsend, msend, asend, ssend = xcopy.copy(), mcopy.copy(), acopy.copy(), scopy.copy()
        if ":" in c:
            eq, c = c.split(":")
            if eq[0] == "x":
                if eq[1] == "<":
                    xsend[1] = int(eq[2:])-1
                    xcopy[0] = int(eq[2:])
                else:
                    xsend[0] = int(eq[2:])+1
                    xcopy[1] = int(eq[2:])
            elif eq[0] == "m":
                if eq[1] == "<":
                    msend[1] = int(eq[2:])-1
                    mcopy[0] = int(eq[2:])
                else:
                    msend[0] = int(eq[2:])+1
                    mcopy[1] = int(eq[2:])
            elif eq[0] == "a":
                if eq[1] == "<":
                    asend[1] = int(eq[2:])-1
                    acopy[0] = int(eq[2:])
                else:
                    asend[0] = int(eq[2:])+1
                    acopy[1] = int(eq[2:])
            elif eq[0] == "s":
                if eq[1] == "<":
                    ssend[1] = int(eq[2:])-1
                    scopy[0] = int(eq[2:])
                else:
                    ssend[0] = int(eq[2:])+1
                    scopy[1] = int(eq[2:])
            else:
                print(c, "xmas error")

        if c == "R":
            pass
        elif c == "A":
            subtotal = (xsend[1]-xsend[0]+1) * (msend[1]-msend[0]+1) * (asend[1]-asend[0]+1) * (ssend[1]-ssend[0]+1)
            print(xsend, msend, asend, ssend)
            print(xcopy, mcopy, acopy, scopy)
            print(subtotal)
            global total
            total += subtotal
            if subtotal < 0:
                print(x, m, a, s)
                print(key, "error")
                exit()

        else:
            tree(c, xsend, msend, asend, ssend)


total = 0
tree("in", [1, 4000], [1, 4000], [1, 4000], [1, 4000])
print(total)

