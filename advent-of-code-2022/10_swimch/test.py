# open the input file
with open("input.txt") as input_file:
  # read the instructions from the file
  instructions = input_file.read().strip().split("\n")

# initialize the X register and the screen
x = 1
screen = [["." for _ in range(40)] for _ in range(6)]

# simulate the execution of the instructions on the CPU
for instruction in instructions:
  # parse the instruction
  op, value = instruction.split()
  value = int(value)

  # execute the instruction
  if op == "addx":
    x += value
  elif op == "noop":
    pass

  # update the screen based on the value of the X register
  left = max(0, x - 1)
  right = min(39, x + 1)
  for y in range(6):
    for x in range(left, right + 1):
      screen[y][x] = "#"

# print the screen to the console
for row in screen:
  print("".join(row))