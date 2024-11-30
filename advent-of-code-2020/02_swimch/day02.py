from prompt_toolkit.layout import max_layout_dimensions

input = []
with open('input.txt', 'r') as f:
    for line in f:
        input.append(line[:-1])


valid_passwords_1 = 0
valid_passwords_2 = 0

for line in input:
    minimum = int(line.split("-")[0])
    maximum = int(line.split("-")[1].split()[0])
    character = line.split()[1][:-1]
    password = line.split()[2]

    ### Part 1 ###
    if minimum <= password.count(character) <= maximum:
        valid_passwords_1 +=1
    ### Part 2 ###
    if (password[minimum-1] == character) ^ (password[maximum-1] == character):
        valid_passwords_2 += 1


print(valid_passwords_1)
print(valid_passwords_2)