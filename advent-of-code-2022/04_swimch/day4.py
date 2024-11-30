import re

with open ('input.txt', 'r') as f:
    input = []
    for line in f:
        input.append(line[:-1])

pairs = []
for line in input:
    pairs.append(re.split(",|-", line))

#### Part 1 ####
counter = 0
for pair in pairs:
    if int(pair[0]) <= int(pair[2]) and int(pair[1]) >= int(pair[3]) or int(pair[0]) >= int(pair[2]) and int(pair[1]) <= int(pair[3]):
        counter += 1
print(counter)

#### Part 2 ####
counter = 0
for pair in pairs:
    if int(pair[0]) <= int(pair[2]) <= int(pair[1]) or int(pair[0]) <= int(pair[3]) <= int(pair[1]) or int(pair[2]) <= int(pair[0]) <= int(pair[3]):
        counter += 1
print(counter)