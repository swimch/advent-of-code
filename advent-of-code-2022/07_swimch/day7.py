import random
structure = {}
size = 0
dir = ""
path = []
counter = 0

with open("input.txt", "r") as f:
    for line in f:
        if line.startswith("$ cd"):
            dir = line.split()[2]
            if dir == "..":
                path.pop()
            else:
                while dir in structure:
                    dir += str(random.randint(1, 9999))
                path.append(dir)
        elif line[0].isdigit(): #loop until doesn't start with digit or dir
            for directory in path:
                if directory in structure:
                    structure[directory] += int(line.split()[0])
                else:
                    structure[directory] = int(line.split()[0])

#### Part 1 ####
for size in structure.values():
    if size <= 100000:
        counter += size
print(counter)

#### Part 2 ####
needed_deleted = structure["/"] - 40000000
potential_dir = [structure[directory] for directory in structure if structure[directory] >= needed_deleted]
potential_dir.sort()
for directory, size in structure.items():
    if size == potential_dir[0]:
        print(structure[directory])
