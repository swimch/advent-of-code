import re

input = []
possible = 0
power = 0


with open('input.txt', 'r') as f:
    for line in f:
        input.append(line[:-1])

for i in range(len(input)):
    sets = (input[i].split(": ")[1].split(";"))
    red = 0
    green = 0
    blue = 0
    for set in sets:
        for pull in set.split(","):
            if "red" in pull:
                red = int(re.findall(r'\d+', pull)[0]) if int(re.findall(r'\d+', pull)[0]) > red else red

            elif "green" in pull:
                green = int(re.findall(r'\d+', pull)[0]) if int(re.findall(r'\d+', pull)[0]) > green else green

            elif "blue" in pull:
                blue = int(re.findall(r'\d+', pull)[0]) if int(re.findall(r'\d+', pull)[0]) > blue else blue

    ### Part 1 ###
    if red < 13 and green < 14 and blue < 15:
        possible += i + 1

    ### Part 2 ###
    power += red * green * blue

print(f"The possible games added are: {possible}")
print(f"The power is: {power}")