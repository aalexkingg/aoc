import re

copies_count = [1 for _ in range(192)]

total = 0
with open("data.txt") as file:
  lines = file.readlines()
  for card_num, line in enumerate(lines):
    numbers = line.split(":")[1].split("|")
    targets = re.findall(r"[\d]+", numbers[0])
    currents = re.findall(r"[\d]+", numbers[1])      

    wins = 0
    for num in currents:
      if num in targets:
        wins += 1

    for i in range(1, wins+1):
      copies_count[card_num+i] += copies_count[card_num]

total = sum(copies_count)
print(total)

