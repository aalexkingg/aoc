total = 0

with open("data.txt") as file:
  lines = file.readlines()
  for line in lines:
    nums = list(filter(str.isdigit, line))
    current = int(nums[0] + nums[-1])
    total += current
    
print(total)

# Part 2

import re

total = 0

numbers = {
  "one":"1",
  "two":"2",
  "three":"3",
  "four":"4",
  "five":"5",
  "six":"6",
  "seven":"7",
  "eight":"8",
  "nine":"9"
}

with open("data.txt") as file:
  lines = file.readlines()
  for line in lines:
    nums = re.findall(r'(?=([\d+]|one|two|three|four|five|six|seven|eight|nine))', line)
    
    if nums[0].isalpha():
      nums[0] = numbers[nums[0]]

    if nums[-1].isalpha():
      nums[-1] = numbers[nums[-1]]

    current = int(nums[0] + nums[-1])
    total += current

print(total)    
