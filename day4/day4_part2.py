import re

with open("puzzle_input.txt", "r") as input_file:
    content = input_file.read().splitlines()

    card_instance = {i: 1 for i in range(len(content))}

    for i, line in enumerate(content):
        match = re.match(r'^.*:\s(.+)\s\|\s(.+)$', line)
        win_set = set(match.group(1).split())
        have_set = set(match.group(2).split())
        
        if (win_have_count := len(win_set.intersection(have_set))):
            for j in range(win_have_count):
                card_instance[i + 1 + j] += card_instance[i]

    print(sum(card_instance.values()))
