import re
import math


def _use_regex(input_text):
    pattern = re.compile(r"[A-Za-z]+")
    return pattern.findall(input_text)


def _read_input(input_file):
    nodes = {}
    with open(input_file, 'r') as f:
        instructions = f.readline()[:-1]
        f.readline()
        for line in f:
            node = (_use_regex(line))
            nodes[node[0]] = {
                "next_left": node[1],
                "next_right": node[2]
            }
    return instructions, nodes


def navigate(input_file, current, destination, ghost):
    instructions, nodes = _read_input(input_file)
    steps = 0
    check = current[2] if ghost else current
    while check != destination:
        for instruction in instructions:
            steps += 1
            if instruction == "L":
                current = nodes[current]["next_left"]
            else:
                current = nodes[current]["next_right"]
            check = current[2] if ghost else current
            if check == destination:
                break
    return steps


def navigate_ghosts(input_file):
    instructions, nodes = _read_input(input_file)
    current_nodes = [x for x in nodes if x[2] == "A"]
    loop_lengths = []
    for current_node in current_nodes:
        loop_lengths.append(navigate(input_file, current_node, "Z", True))
    steps = math.lcm(*loop_lengths)
    return steps


print(f'The number of required steps for a human are: {navigate("input.txt", "AAA", "ZZZ", False)}')
print(f'The number of required steps for a ghost are: {navigate_ghosts("input.txt")}')
