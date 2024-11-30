input = []
kalorien = 0
suchtrupp = []

with open ('input.txt', 'r') as f:
    for line in f:
        input.append(line[:-1])

for line in input:
    if line != "":
        kalorien += int(line)
    else:
        suchtrupp.append(kalorien)
        kalorien = 0
suchtrupp.sort(reverse=True)

#### Part1 ####
print(suchtrupp[0])

#### Part2 ####
print(sum(suchtrupp[:3:]))