def get_part(line, j, dir):
        if not line[j].isdigit():
            return
        left = right = j
        if dir in ("both", "left"):
            while left > 0 and line[left - 1].isdigit():
                left -= 1
        if dir in ("both", "right"):
            while right < len(line) - 1 and line[right + 1].isdigit():
                right += 1
        return line[left:right + 1]

def vertical_get_part(content, i, j, di, parts):
    if (vertical := get_part(content[i + di], j, "both")):
        parts.append(vertical)
    else:
        if j > 0 and (vertical_left := get_part(content[i + di], j - 1, "left")):
            parts.append(vertical_left)
        if j < len(line) - 1 and (vertical_right := get_part(content[i + di], j + 1, "right")):
            parts.append(vertical_right)

with open("puzzle_input.txt", "r") as input_file:
    content = input_file.read().splitlines()

    res = 0

    for i, line in enumerate(content):
        for j, char in enumerate(line):
            if char == '*':
                parts = []

                if i != 0:
                    vertical_get_part(content, i, j, -1, parts)

                if i < len(content) - 1:
                    vertical_get_part(content, i, j, 1, parts)
                
                if j != 0 and (left := get_part(content[i], j - 1, "left")):
                    parts.append(left)
                
                if j != len(line) - 1 and (right := get_part(content[i], j + 1, "right")):
                    parts.append(right)

                if len(parts) == 2:
                    res += int(parts[0]) * int(parts[1])
                
    print(res)