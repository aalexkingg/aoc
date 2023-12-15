
with open("data") as f:
    line = f.readlines()[0]
    data = line.strip("\n").split(",")
    total = 0
    for item in data:
        current_value = 0
        for char in item:
            current_value += ord(char)
            current_value *= 17
            current_value = current_value % 256
        print(item, current_value)
        total += current_value
    print(total)
