import re

total = 0
with open("data.txt") as file:
  for line in file.readlines():
    numbers = line.split(":")[1].split("|")
    targets = re.findall(r"[\d]+", numbers[0])
    currents = re.findall(r"[\d]+", numbers[1])
    
    current_total = 0
    for num in currents:
      if num in targets:
        if current_total == 0:
          current_total = 1
        else:
          current_total = current_total * 2
    total += current_total
print(total)

