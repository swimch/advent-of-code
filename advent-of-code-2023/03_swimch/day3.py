input_data = []
with open('input.txt', 'r') as f:
    for line in f:
        input_data.append(line[:-1])

rows = len(input_data)
columns = len(input_data[0])


# 💀
def stay_in_range(row, column):
    if row == 0:
        over = 0
        under = 2
    elif row == rows - 1:
        over = -1
        under = 1
    else:
        over = -1
        under = 2

    if column == 0:
        left = 0
        right = 2
    elif column == columns - 1:
        left = -1
        right = 1
    else:
        left = -1
        right = 2
    return over, under, left, right


# check if surrounding chars are special chars
def check_for_special(row, column):
    # staying in range
    over, under, left, right = stay_in_range(row, column)
    for y in range(over, under):
        for x in range(left, right):
            if not input_data[row + y][column + x].isdigit() and not input_data[row + y][column + x] == ".":
                return True


def check_for_gear(positions):
    for position in positions:
        row = position[0]
        column = position[1]
        over, under, left, right = stay_in_range(row, column)
        for y in range(over, under):
            for x in range(left, right):
                if input_data[row + y][column + x] == "*":
                    if ((row + y), (column + x)) in gears:
                        gears[(row + y, column + x)].append(numbers[positions])
                    else:
                        gears[(row + y, column + x)] = [numbers[positions]]
                    return


cache = ""
is_part = False
parts = []
coordinates = []
numbers = {}
gears = {}

# loop through input and check if numbers are parts, also stores coordinates of all numbers for part 2
for i in range(len(input_data)):
    for j in range(len(input_data[i])):
        # if digit -> add to cache and check surroundings
        if input_data[i][j].isdigit():
            cache += input_data[i][j]
            coordinates.append((i, j))
            if not is_part:
                is_part = check_for_special(i, j)
        # if not a digit but is_part == True -> part ended here and add cache to parts
        elif is_part:
            parts.append(int(cache))
            numbers[tuple(coordinates)] = cache
            coordinates = []
            cache = ""
            is_part = False
        # wasn't a part and not a digit -> empty cache
        else:
            coordinates = []
            cache = ""

# part 1
print(f"the sum of the parts is: {sum(parts)}⚙️🔩🔧")

# part 2
for pos in numbers:
    check_for_gear(pos)

gear_ratio = 0
for gear in gears:
    if len(gears[gear]) == 2:
        gear_ratio += int(gears[gear][0]) * int(gears[gear][1])

print(f"The gear ratio is: {gear_ratio}💀")
