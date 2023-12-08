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

pattern = f"(?=({'|'.join(digit_str_to_int.keys())}|\d))"

with open("puzzle_input.txt", "r") as input_file:
    sum = 0

    for line in input_file:
        hits = [str(digit_str_to_int.get(match, match)) for match in re.findall(pattern, line)]
        sum += int(hits[0] + hits[-1])

    print(sum)