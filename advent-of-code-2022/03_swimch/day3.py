input = []

with open ('input.txt', 'r') as f:
    for line in f:
        input.append(line[:-1])

def char_to_num(char):
        if ord(char) > 96:
            num = ord(char) - 96
        else:
            num = ord(char) - 38
        return(num)

#### Part 1 ####
backpacks = []
epic_fails = []
priority  = 0

for line in input:
    compartment1 = line[:len(line)//2]
    compartment2 = line[len(line)//2:]
    backpacks.append((compartment1, compartment2))

for backpack in backpacks:
    for item in backpack[0]:
        if item in backpack[1]:
            priority += char_to_num(item)
            break

print(priority)

#### Part 2 ####
badges = 0

for i in range(0,len(input)-2,3):
    for item in input[i]:
        if item in input[i+1] and item in input[i+2]:
            badges += char_to_num(item)
            break            

print(badges)