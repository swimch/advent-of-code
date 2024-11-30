f = open("input.txt", "r")
input = [line.strip() for line in f]

strenght = 0
cycle = 0
x = int
def strenght_check(cycle, x):
    global strenght
    if cycle == 20 or (cycle - 20) % 40 == 0:
        strenght += cycle * x
    return strenght

image = ""
row = 0
def imaging(cycle, x):
    global image
    global row
    if cycle % 40 == 0:
        row += 1
    cycle_image = cycle - (40*row)
    if cycle_image in [x-1, x, x+1]:
        image += "#"
    else:
        image += "."
    if (cycle - 1) % 40 == 39:
        image += "\n"
    return image


def iterate(function, input, x):
    cycle = 0
    for command in input:
        if command.startswith("noop"):
            cycle += 1
            printer = function(cycle, x)
        elif command.startswith("addx"):
            cycle += 1
            printer = function(cycle, x)
            cycle += 1
            printer = function(cycle, x)
            x += int(command.split()[1])
    return printer

print(iterate(strenght_check, input, 1))
print(iterate(imaging, input, 2)) #wtf warum muss x 2 sie?!
