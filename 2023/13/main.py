def column(b, c):
    if c < 0:
        raise IndexError
    temp = ""
    for bl in blocks[b]:
        temp += bl[c]
    return temp


def find_differences(str1, str2):
    diffs = 0
    for d in range(len(str1)):
        if str1[d] != str2[d]:
            diffs += 1
    return diffs


with open("data.txt") as f:
    lines = f.readlines()
    block = 0
    blocks = [[]]
    total = 0
    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n")

        if lines[i]:
            blocks[block].append(lines[i])
        else:
            block += 1
            blocks.append([])

    for b in range(100):
        score = 0
        # rows
        for row in range(len(blocks[b])-1):
            diffs = 0
            try:
                for i in range(0, row+2):
                    if row-i < 0:
                        raise IndexError
                    diffs += find_differences(blocks[b][row-i], blocks[b][row+i+1])
            except IndexError:
                if diffs == 1:
                    score = (row+1) * 100
                    total += score
                    break

        if not score:
            # columns
            for col in range(len(blocks[b][0])-1):
                diffs = 0
                try:
                    for i in range(0, col+2):
                        diffs += find_differences(column(b, col-i), column(b, col+1+i))
                except IndexError:
                    if diffs == 1:
                        score = col + 1
                        total += score
                        break

    print(total)
