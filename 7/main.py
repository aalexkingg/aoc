import numpy as np

cards = np.empty((1000, 3), dtype=object)

with open("data.txt") as file:
  lines = file.readlines()

  for line_num, line in enumerate(lines):
    cards[line_num][1] = str(line.split(" ")[0])
    cards[line_num][2] = int(line.split(" ")[1])

    # grade
    sets = list(set(cards[line_num][1]))
    hand = list(cards[line_num][1])
    x = len(sets)
    if x == 1:
      cards[line_num][0] = 7

    elif x == 2:
      if hand.count(sets[0]) == 4 or hand.count(sets[1]) == 4:
        cards[line_num][0] = 6
      else:
        cards[line_num][0] = 5
      if "1" in hand:
        cards[line_num][0] = 7

    elif x == 3:
      if hand.count(sets[0]) == 3 or hand.count(sets[1]) == 3 or hand.count(sets[2]) == 3:
        cards[line_num][0] = 4
        if "1" in hand:
          cards[line_num][0] = 6
      else:
        cards[line_num][0] = 3
        if "1" in hand:
          if hand.count("1") == 2:
            cards[line_num][0] = 6
          else:
            cards[line_num][0] = 5

    elif x == 4:
      cards[line_num][0] = 2
      if "1" in hand:
        cards[line_num][0] = 4

    else:
      cards[line_num][0] = 1
      if "1" in hand:
        cards[line_num][0] = 2



test = sorted(cards, key=lambda x: (x[0],x[1]))

total = 0
for index, card in enumerate(test):
  print(card[0], card[1])
  total += (index+1) * card[2]

print(total)