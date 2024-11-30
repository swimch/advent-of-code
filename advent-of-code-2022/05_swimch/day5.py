import numpy as np

line_n = 0
row = []
crates = []
instructions = []
with open ('input.txt', 'r') as file:
    for line in file:
        line_n += 1
        if line[0] == "[": #Kisten
            for i in range(1,len(line)-2,4):
                if line[i] != " ":
                    row.append(line[i])
                else:
                    row.append(None)
            crates.append(row)
            row = []
        elif line_n > 10: #Anweisungen
            instructions.append([int(item) for item in line.split() if item.isdigit()])

#Rotate 90° & remove None
crates = np.asanyarray(crates)
crates = np.rot90(crates, 3)
crates = crates.tolist()
crates_cleaned = []
for column in crates:
    column_cleaned = [item for item in column if item is not None]
    crates_cleaned.append(column_cleaned)

def get_message(crates):
    message = ""
    for column in crates:
        if column != []:
            message += column[-1]
        else:
            message += " "
    print(message)

#### Part 1 ####
crates_cleaned_copy = crates_cleaned.copy()
for instr in instructions:
    for i in range(instr[0]):
        crates_cleaned_copy[instr[2]-1].append(crates_cleaned_copy[instr[1]-1].pop())
get_message(crates_cleaned_copy)

#### Part 2 ####
crates_cleaned_copy = crates_cleaned.copy()
for instr in instructions:
    mover = crates_cleaned_copy[instr[1]-1][-instr[0]:]
    for item in mover:
        crates_cleaned_copy[instr[2]-1].append(item)
    del crates_cleaned_copy[instr[1]-1][-instr[0]:]
get_message(crates_cleaned_copy)