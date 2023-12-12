import re

total = 0
temp_total = 0

with open("data.txt", 'r') as file:
  lines = file.readlines()

  for index, line in enumerate(lines):
    lines[index] = "." + line.replace('\n', '') + "."
  
  for line_num, line in enumerate(lines):
    nums = re.finditer(r"[\d]+", line)
    print("Line num: ",line_num)

    for num in nums:
      valid = False

      rnge = (num.span()[0]-1, num.span()[1]+1)

      # search above
      if line_num > 0:
        for i in range(*rnge):
          if lines[line_num-1][i] != ".":
            valid = True

      # search either side of number for dot, if no dot, num = 0
      if line[num.span()[0]-1] != ".":
        valid = True

      if line[num.span()[1]] != ".":
        valid = True
      
      # search below
      if line_num < 141:
        for i in range(*rnge):
          if lines[line_num+1][i] != ".":
            valid = True

      if valid:
        print(int(num.group(0)))
        total += int(num.group(0))

print(total)
