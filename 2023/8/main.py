
directions = {}
route = "00111001110111010100110111000101110111010011011100110110101110110010110111011001110100010111011000011101110111010110110101100100111011010011011001001011101010111011000101110010011101010111001000011101110101110110110010101110111010110000101110111010111010110101111"

with open("data.txt") as file:
    lines = file.readlines()
    for line in lines:
        directions[line[0:3]] = (line[7:10], line[12:15])

    current = ['AAA', 'DPA', 'QLA', 'VJA', 'GTA', 'XQA']

    for i in range(6):
        steps = 0
        while True:
            direction = int(route[steps % 263])
            current[i] = directions[current[i]][direction]
            steps += 1

            # Find LCM of the 6 output numbers
            if current[i][2] == 'Z':
                print(steps, current[i])
                break
