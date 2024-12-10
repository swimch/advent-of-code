top_map = []
with open("input.txt", "r") as f:
    for line in f:
        top_map.append(line.strip())
height = len(top_map) - 1   # to stay in bounds when checking surroundings
width = len(top_map[0]) - 1

def check_surrounding(pos, check):
    directions = ((1,0), (-1,0), (0,1), (0,-1)) # check direct neighbours, not diagonally
    next_positions = [] # save positions for all positive checks
    for dy, dx in directions:
        if 0 <= pos[0] + dy <= height and 0 <= pos[1] + dx <= width and top_map[pos[0] + dy][pos[1] + dx] == check:
             next_positions.append((pos[0] + dy, pos[1] + dx))
    return next_positions

def count_trails(pos):
    pos = [pos]
    for next_char in range(1,10): # check if valid from 1 through 9
        next_pos = [] # empty this list
        for check_pos in pos:
            next_pos += check_surrounding(check_pos, str(next_char))
        pos = next_pos # create list for next passthrough
        if not pos: return 0 # early return if all paths were invalid
    return set(pos) # only return each summit once

def rate_trails(pos):
    paths = 1 # trailhead starts with one path
    prev_paths = 1
    pos = [pos]
    for next_char in range(1,10): # check if valid from 1 through 9
        next_pos = [] # empty this list
        for check_pos in pos:
            next_pos += check_surrounding(check_pos, str(next_char))
        paths += len(next_pos) - prev_paths # only add additional paths by subtracting previous number of paths
        prev_paths = len(next_pos) # gets number of current paths
        pos = next_pos # create list for next passthrough
        if not pos: return 0
    return paths

trails, ratings = 0, 0
for i, line in enumerate(top_map):
    for j, char in enumerate(line):
        if char == "0":
            trails += len(count_trails((i, j)))
            ratings += rate_trails((i, j))
print(f"There are {trails} valid trails.")
print(f"The combined rating of all valid trailheads is: {ratings}")