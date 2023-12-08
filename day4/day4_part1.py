import re

with open("puzzle_input.txt", "r") as input_file:
    res = 0

    for line in input_file:
        match = re.match(r'^.*:\s(.+)\s\|\s(.+)$', line)
        win_set = set(match.group(1).split())
        have_set = set(match.group(2).split())

        if (win_have_count := len(win_set.intersection(have_set))):
            res += 2 ** (win_have_count - 1)

    print(res)
