import re

total = 0

with open("data.txt") as file:
  lines = file.readlines()
  for line in lines:

    comp = re.compile(r"[(\d+) (red|green|blue)]+")
    finds = re.findall(comp, line)
    temp = [find.split(" ") for find in finds]

    game = int(temp[0][1])

    red, green, blue = 0, 0, 0
    
    for t in temp[1:]:
      if t[2] == "red" and int(t[1]) > red:
        red = int(t[1])
      elif t[2] == "green" and int(t[1]) > green:
        green = int(t[1])
      elif t[2] == "blue" and int(t[1]) > blue:
        blue = int(t[1])

    total += (red * green * blue)
    
print(total)
