
def get_hash(lab):
    tot = 0
    for char in lab:
        tot += ord(char)
        tot *= 17
        tot = tot % 256
    return tot


with open("data") as f:
    line = f.readlines()[0]
    data = line.strip("\n").split(",")

    boxes = [{} for _ in range(256)]
    for item in data:
        if "=" in item:
            label, num = item.split("=")
            hashed = get_hash(label)
            boxes[hashed][label] = int(num)
        else:
            label = item[:-1]
            hashed = get_hash(label)
            try:
                del boxes[hashed][label]
            except KeyError:
                pass

    total = 0
    for i in range(256):
        if boxes[i]:
            box_tot = 0
            for slot, num in enumerate(boxes[i].values()):
                box_tot += (i+1) * (slot+1) * num
            total += box_tot
            print(i+1, box_tot)
    print(total)

