antennas = {}
with open('input.txt', 'r') as f:
    length = -1
    for i, line in enumerate(f):
        length += 1
        line_length = len(line[:-2])
        for j, position in enumerate(line[:-1]):
            if position != '.':
                if position not in antennas:
                    antennas[position] = []
                antennas[position].append((i, j))
    # roofs = tuple((line[:-1]) for line in f)
# print(length, line_length) # 50, 50

def harmonics(pos1, pos2, dif):
    harmonic = []
    if pos1 != pos2:
        pos = pos1
        while pos[0] >= 0 and 0 <= pos[1] <= line_length:
            pos = (pos[0] - dif[0], pos[1] - dif[1])
            harmonic.append(pos)
        pos = pos2
        while pos[0] <= length and 0 <= pos[1] <= line_length:
            pos = (pos[0] + dif[0], pos[1] + dif[1])
            harmonic.append(pos)
    else:
        return tuple([pos1])
    return harmonic

antinodes2 = []
antinodes = []
for positions in antennas.values():
    for position in positions:
        for second_position in positions:
            difference = (second_position[0] - position[0], second_position[1] - position[1])
            if difference != (0, 0):
                antinodes.append((position[0] - difference[0], position[1] - difference[1]))
                antinodes.append((second_position[0] + difference[0], second_position[1] + difference[1]))
            antinodes2 += [harmonic for harmonic in harmonics(position, second_position, difference)]


antinodes = {antinode for antinode in antinodes if 0 <= antinode[0] <= length and 0 <= antinode[1] <= line_length}
print(len(antinodes)) # 276
antinodes2 = {antinode for antinode in antinodes2 if 0 <= antinode[0] <= length and 0 <= antinode[1] <= line_length}
print(len(antinodes2)) # 991