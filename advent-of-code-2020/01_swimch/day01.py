input = []
with open('input.txt', 'r') as f:
    for line in f:
        input.append(int(line[:-1]))

### Part 1 ###
input_1 = input[:]
for zahl in input_1:
    input_1.pop(0)
    for zahl_zwei in input_1:
        if zahl + zahl_zwei == 2020:
            print(zahl * zahl_zwei)

### Part 2 ###
input_2 = input[:]
for zahl in input_2:
    input_2.pop(0)
    for zahl_zwei in input_2:
        for zahl_drei in input_2:
            if zahl + zahl_zwei + zahl_drei == 2020:
                print(zahl * zahl_zwei * zahl_drei)