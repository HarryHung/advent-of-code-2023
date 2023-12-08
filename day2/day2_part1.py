import re

bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def compare_to_bag(set):
    for colour, count in bag.items():
        matched_count = re.search(rf"\d+(?=\s{colour})", set)
        if matched_count and int(matched_count.group(0)) > count:
            return False
    return True

with open("puzzle_input.txt", "r") as input_file:
    res = 0

    for i, line in enumerate(input_file):
        if all(compare_to_bag(set) for set in line.split(": ")[1].split("; ")):
            res += i + 1
    
    print(res)