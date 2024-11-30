import string
abc = string.ascii_lowercase

file = []
with open('input.txt', 'r') as f:
    for line in f:
        file.append(line[:-1])

group = ""
count = 0
count_2 = 0
group_size = 0
for line in file:
    if line == "":
        count += sum([1 for a in abc if a in group]) # Check if anyone answered yes in group
        count_2 += sum([1 for a in abc if group.count(a) == group_size]) # Check if everyone answered yes in group
        group = ""
        group_size = 0
    else:
        group_size += 1
        group += line
count += sum([1 for a in abc if a in group]) # To also count the last group
count_2 += sum([1 for a in abc if group.count(a) == group_size]) # To also count the last group

print(f"The count for part 1 is {count}")
print(f"The count for part 2 is {count_2}")
