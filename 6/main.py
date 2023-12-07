import re

times = [53897698]
distances = [313109012141201]

result = 1

for i in range(len(times)):
  fails = 0
  for j in range(times[i]):
    if j * (times[i]-j) > distances[i]:
      result *= (times[i] + 1 - (2*fails))
      break
    else:
      fails += 1

print(result)

  
  
