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
                    if c == "A":
                        global total
                        total += (x[1]-x[0]+1) * (m[1]-m[0]+1) * (a[1]-a[0]+1) * (s[1]-s[0]+1)
                    elif c == "R":
                        x[0] = int(eq[2:])
                    else:
                        tree(c, [int(eq[2:])-1, x[1]], m, a, s)
                        x[0] = int(eq[2:])
                else:
                    if c == "A":
                        global total
                        total += (x[1]-x[0]+1) * (m[1]-m[0]+1) * (a[1]-a[0]+1) * (s[1]-s[0]+1)
                    elif c == "R":
                        x[0] = int(eq[2:])
                    else:
                        tree(c, [int(eq[2:])+1, x[1]], m, a, s)
                        x[0] = int(eq[2:])
            elif eq[0] == "m":
                if eq[1] == "<":
                    if c == "A":
                        global total
                        total += (x[1]-x[0]+1) * (m[1]-m[0]+1) * (a[1]-a[0]+1) * (s[1]-s[0]+1)
                    elif c == "R":
                        m[0] = int(eq[2:])
                    else:
                        tree(c, x, [int(eq[2:])-1, m[1]], a, s)
                        m[0] = int(eq[2:])
                else:
                    if c == "A":
                        global total
                        total += (x[1]-x[0]+1) * (m[1]-m[0]+1) * (a[1]-a[0]+1) * (s[1]-s[0]+1)
                    elif c == "R":
                        m[0] = int(eq[2:])
                    else:
                        tree(c, x, [int(eq[2:])+1, m[1]], a, s)
                        m[0] = int(eq[2:])
            elif eq[0] == "a":
                if eq[1] == "<":
                    if c == "A":
                        global total
                        total += (x[1]-x[0]+1) * (m[1]-m[0]+1) * (a[1]-a[0]+1) * (s[1]-s[0]+1)
                    elif c == "R":
                        a[0] = int(eq[2:])
                    else:
                        tree(c, x, m, [int(eq[2:])-1, a[1]], s)
                        a[0] = int(eq[2:])
                else:
                    if c == "A":
                        global total
                        total += (x[1]-x[0]+1) * (m[1]-m[0]+1) * (a[1]-a[0]+1) * (s[1]-s[0]+1)
                    elif c == "R":
                        a[0] = int(eq[2:])
                    else:
                        tree(c, x, m, [int(eq[2:])+1, a[1]], s)
                        a[0] = int(eq[2:])
            elif eq[0] == "s":
                if eq[1] == "<":
                    if c == "A":
                        global total
                        total += (x[1]-x[0]+1) * (m[1]-m[0]+1) * (a[1]-a[0]+1) * (s[1]-s[0]+1)
                    elif c == "R":
                        s[0] = int(eq[2:])
                    else:
                        tree(c, x, m, a, [int(eq[2:])-1, s[1]])
                        s[0] = int(eq[2:])
                else:
                    if c == "A":
                        global total
                        total += (x[1]-x[0]+1) * (m[1]-m[0]+1) * (a[1]-a[0]+1) * (s[1]-s[0]+1)
                    elif c == "R":
                        s[0] = int(eq[2:])
                    else:
                        tree(c, x, m, a, [int(eq[2:])+1, s[1]])
                        s[0] = int(eq[2:])
            else:
                print(c, "xmas error")

        if c == "R":
            pass
        elif c == "A":
            global total
            total += (x[1] - x[0] + 1) * (m[1] - m[0] + 1) * (a[1] - a[0] + 1) * (s[1] - s[0] + 1)
        else:
            tree(c, x, m, a, s)


total = 0
tree("in", [1, 4000], [1, 4000], [1, 4000], [1, 4000])
print(total)

