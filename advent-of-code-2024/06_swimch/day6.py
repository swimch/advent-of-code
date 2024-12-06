input = []
with open('input.txt', 'r') as f:
    for line in f:
        input.append([char for char in line[:-1]])


def guard_route(lab, guard_pos): # map of lab and guard start position
    path = {} # dictionary to store route and to check for loops in it
    direction = (-1, 0) # set initial direction (y, x) coordinates
    while True: # loop until out of lab or path is a loop
        if guard_pos not in path: path[guard_pos] = [direction] # check if guard was already at current position
        elif direction in path[guard_pos]: return "loop" # if current direction is in current position -> path is a loop
        else: path[guard_pos].append(direction) # add direction to position in dictionary

        # check if she moves out of lab
        if not (0 <= guard_pos[0] + direction[0] < len(lab) and 0 <= guard_pos[1] + direction[1] < len(lab[0])):
            return path
        if lab[guard_pos[0]+direction[0]][guard_pos[1]+direction[1]] != '#': # checks if next field is obstructed
            guard_pos = guard_pos[0]+direction[0], guard_pos[1]+direction[1] # move guard
        else: # if obstructed
            direction = direction[1], -direction[0] # rotate guard by 90 degrees

for i, line in enumerate(input):  # finds start for guard
    for j, char in enumerate(line):
        if char == "^":
            guard = i, j

route = guard_route(input, guard) # gets route dictionary for normal path

loops = 0 # count how many loops are possible
for path_pos in route: # only obstructs fields on normal path
    if path_pos != guard: # don't obstruct start field
        obstructed_route = [[char for char in line] for line in input] # create copy of map
        obstructed_route[path_pos[0]][path_pos[1]] = "#" # obstruct one field
        if guard_route(obstructed_route, guard) == "loop":
            loops += 1

# runtime: 9s
print(f"The guard moves over {len(route)} fields until she moves off the map") # 4711
print(f"There are {loops} possible loops by obstruction to get past the guard") # 1562
