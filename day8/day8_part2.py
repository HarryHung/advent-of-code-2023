import re
import math


def get_loop_length(node, nav_map, instruction):
    length, instruction_length = 0, len(instruction)

    while not node.endswith('Z'):
        node = nav_map[node][0] if instruction[length % instruction_length] == 'L' else nav_map[node][1]
        length += 1

    return length 

with open("puzzle_input.txt", "r") as input_file:
    lines = input_file.readlines()

    instruction = lines[0].strip()

    nav_map = {}
    for line in map(str.strip, lines[2:]):
        matches = re.match(r'^(\w{3})\s=\s\((\w{3}), (\w{3})\)$', line)
        nav_map[matches.group(1)] = (matches.group(2), matches.group(3))
    
    starting_nodes = [node for node in nav_map if node.endswith('A')]

    print(math.lcm(*[get_loop_length(node, nav_map, instruction) for node in starting_nodes]))