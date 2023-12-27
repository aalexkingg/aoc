data = [x for x in open("data").read().strip().split("\n")]

total = 0
for i, d in enumerate(data[:-1]):
    pos, vel = [[int(y) for y in x.split(", ")] for x in d.split(" @ ")]

    x1_pos, y1_pos = pos[0], pos[1]
    x1_dir, y1_dir = vel[0], vel[1]
    count = 0

    xy1 = vel[0] / vel[1]
    xz1 = vel[0] / vel[2]

    for nd in data[i+1:]:
        npos, nvel = [[int(y) for y in x.split(", ")] for x in nd.split(" @ ")]

        xy2 = nvel[0] / nvel[1]
        xz2 = nvel[0] / nvel[2]

        x2_pos, y2_pos = npos[0], npos[1]
        x2_dir, y2_dir = nvel[0], nvel[1]

        xpos, ypos = x2_pos-x1_pos, y2_pos-y1_pos


        try:
            mu = -(xpos * y1_dir - ypos * x1_dir) / (x2_dir * y1_dir - y2_dir * x1_dir)

        except ZeroDivisionError:
            #print(vel, nvel)
            continue

        xlam = (xpos + mu * x2_dir) / x1_dir
        ylam = (ypos + mu * y2_dir) / y1_dir

        min, max = 200000000000000, 400000000000000
        #min, max = 7, 21
        if abs(xlam-ylam) < 1 and mu >= 0 and xlam >= 0:
            xcoord = x1_pos + xlam * x1_dir
            ycoord = y1_pos + ylam * y1_dir

            if min <= xcoord <= max and min <= ycoord <= max:
                total += 1

print(total)
