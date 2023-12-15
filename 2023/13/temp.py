from functools import reduce
from helpers import base_convert

temp = base_convert(125, 5, 8)
print(temp)

nums = [14, 10, 9]

t = reduce(lambda x, y: nums.index(x) if x > 10 else len(nums)+1, nums)
print(t)

arr = ["aaa", "bbb", "ccc"]

print(list(map(list, zip(*arr))))
