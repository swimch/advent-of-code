import time
t1 = time.time()
with open ('input.txt') as f:
    lines = f.readlines()
    
instructions = [int(x) for x in lines[0].split(",")]
def check(pos1, pos2):
    commands = instructions.copy()
    commands[1] = pos1
    commands[2] = pos2
    for i in range(0, len(commands), 4):
        if commands[i] == 1:
            commands[commands[i+3]] = commands[commands[i+1]] + commands[commands[i+2]]
        elif commands[i] == 2:
            commands[commands[i+3]] = commands[commands[i+1]] * commands[commands[i+2]]
        elif commands[i] == 99:
            return(commands[0])

#### Part1 ####
print(check(12, 2))

#### Part2 ####
for noun in range(1, 100):
    for verb in range(1, 100):
        if check(noun, verb) == 19690720:
            print(100 * noun + verb)

t2 = time.time() - t1
print(t2)