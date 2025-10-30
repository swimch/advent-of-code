input = []

with open ('input', 'r') as f:
    for line in f:
        input.append(line[:-1])


def part1():
    frequency = 0
    for change in input:
        frequency = frequency + int(change[1:]) if change[0] == "+" else frequency - int(change[1:])
    return frequency

def part2():
    frequencies = [0]
    frequency = 0
    while True:
        for change in input:
            frequency = frequency + int(change[1:]) if change[0] == "+" else frequency - int(change[1:])
            if frequency in frequencies:
                return frequency
            frequencies.append(frequency)


print(part1())
print(part2())
