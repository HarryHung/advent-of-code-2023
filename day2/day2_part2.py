import re
from functools import reduce

with open("puzzle_input.txt", "r") as input_file:
    res = 0

    for i, line in enumerate(input_file):
        min_set = {
            "blue": 0,
            "red": 0,
            "green": 0
        }

        for set in line.split(": ")[1].split("; "):
            for colour in min_set:
                if matched_count := (re.search(rf"\d+(?=\s{colour})", set)):
                    min_set[colour] = max(int(matched_count.group(0)), min_set[colour])
        
        res += reduce(lambda x, y: x * y, min_set.values())
    
    print(res)