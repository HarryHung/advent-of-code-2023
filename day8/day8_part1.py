import re

with open("puzzle_input.txt", "r") as input_file:
    lines = input_file.readlines()

    instruction = lines[0].strip()
    instruction_length = len(instruction)

    nav_map = {}
    for line in map(str.strip, lines[2:]):
        matches = re.match(r'^([A-Z]{3})\s=\s\(([A-Z]{3}), ([A-Z]{3})\)$', line)
        nav_map[matches.group(1)] = (matches.group(2), matches.group(3))
    
    res = 0
    cur = 'AAA'
    while cur != 'ZZZ':
        cur = nav_map[cur][0] if instruction[res % instruction_length] == 'L' else nav_map[cur][1]
        res += 1

    print(res)