import re

memory = ""
for line in open('input.txt').read().splitlines():
    memory += line

instructions = re.findall(r"mul\((\d+),(\d+)\)", memory)
instructions2 = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", memory)

result1 = 0
for instruction in instructions:
    result1 += int(instruction[0])*int(instruction[1])

result2 = 0,
do = True
for instruction in instructions2:
    if instruction[2] == "do()":
        do = True
    elif instruction[3] == "don't()":
        do = False
    elif do:
        print(instruction)
        result2 += int(instruction[0])*int(instruction[1])

print(result1)
print(result2)