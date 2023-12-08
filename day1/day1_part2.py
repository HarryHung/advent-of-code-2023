import re

digit_str_to_int = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

with open("puzzle_input.txt", "r") as input_file:
    sum = 0

    for line in input_file:
        hits = []
        for i, c in enumerate(line):
            if c.isdigit():
                hits.append(str(c))
                continue

            for digit_str, digit_int in digit_str_to_int.items():
                if line[i:].startswith(digit_str):
                    hits.append(str(digit_int))
                    break
        
        sum += int(hits[0] + hits[-1])

    print(sum)