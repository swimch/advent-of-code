with open('input.txt', 'r') as f:
    for line in f:
        computer = line[:-1]

storage = [] # files and empty storage are saved for part 1
empty = [] # index list for empty spaced for part 1
files = [] # files stored as file blocks for part 2
empty2 = [] # empty blocks for part 2
i = 0 # index for file names
j = 0 # index for list with empty space
is_file = True # alternate between files and empty spaces
for char in computer:
    if is_file:
        storage += [i for _ in range(int(char))]
        files.append([int(char), j, i]) # file length, position in storage, file name
        i += 1 # file name
        j += int(char) # index in storage for empty positions
    else:
        storage += ["." for _ in range(int(char))]
        empty += [k for k in range(j, j + int(char))]
        empty2.append([int(char), j]) # empty block length, position in storage
        j += int(char) # index in storage for empty positions
    is_file = False if is_file else True # toggle

for i, num in enumerate(storage[::-1]):
    # check if index of file is larger than index of empty space
    if num != "." and empty and len(storage) - i - 1 > empty[0]:
        storage[empty.pop(0)] = num # change file position
        storage[len(storage) - i - 1] = "."

result1 = 0
for i, num in enumerate(storage):
    if num != ".":
        result1 += i * num
print(result1)


result2 = 0
for file in files[::-1]:
    for block in empty2:
        if block[1] < file[1] and block[0] >= file[0]: # check if file block fits in an empty block with smaller index
            file[1] = block[1] # change position of file block
            # remove filled spaced from empty block, beginning in the front
            block[0], block[1] = block[0] - file[0], block[1] + file[0]
            break # only move file once
    result2 += sum([(file[1]+i) * file[2] for i in range(file[0])])
print(result2)