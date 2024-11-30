import math
input = []
fuelformodule = 0
fuelforfuel = 0
fueltank = 0
wish = False

with open ('input.txt', 'r') as f:
    for line in f:
        input.append(line[:-1])
    
#### Part1 & 2 ####
for line in input:
    addfuel = math.floor(int(line)/3)-2
    fuelformodule += addfuel
    fuelforfuel = math.floor(addfuel/3)-2
    while fuelforfuel > 0:
        fueltank+= fuelforfuel
        fuelforfuel = math.floor(fuelforfuel/3)-2
print(fuelformodule)
print(fuelformodule + fueltank)

