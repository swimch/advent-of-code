file = []
with open('input.txt', 'r') as f:
    for line in f:
        file.append(line[:-1])

# -1 because index starts at 0
width = len(file[0]) - 1

# y_step default = 1
def tree_checker(x_step, y_step=1):
    trees = 0
    x_pos = 0
    # checklist = file[start_index:end_index:step]
    check_list = file[::y_step]
    for f_line in check_list:
        if f_line[x_pos] == "#":
            trees += 1
        x_pos += x_step
        # loop back to the left, forest repeats
        if x_pos > width:
            x_pos = x_pos % (width + 1)
    return trees
### Part 1 ###
print(tree_checker(3, 1))
### Part 2 ###
print(tree_checker(1)*tree_checker(3)*tree_checker(5)*tree_checker(7)*tree_checker(1,2))


