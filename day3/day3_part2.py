with open("puzzle_input.txt", "r") as input_file:
    content = input_file.read().splitlines()

    res = 0

    def look(line, j, dir):
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

    for i, line in enumerate(content):
        for j, char in enumerate(line):
            if char == '*':
                parts = []
                if i != 0:
                    if (up := look(content[i - 1], j, "both")):
                        parts.append(up)
                    else:
                        if j > 0 and (up_left := look(content[i - 1], j - 1, "left")):
                            parts.append(up_left)
                        if j < len(line) - 1 and (up_right := look(content[i - 1], j + 1, "right")):
                            parts.append(up_right)
                            
                if i < len(content) - 1:
                    if (down := look(content[i + 1], j, "both")):
                        parts.append(down)
                    else:
                        if j > 0 and (down_left := look(content[i + 1], j - 1, "left")):
                            parts.append(down_left)
                        if j < len(line) - 1 and (down_right := look(content[i + 1], j + 1, "right")):
                            parts.append(down_right)
                
                if j != 0 and (left := look(content[i], j - 1, "left")):
                    parts.append(left)
                
                if j != len(line) - 1 and (right := look(content[i], j + 1, "right")):
                    parts.append(right)

                if len(parts) == 2:
                    res += int(parts[0]) * int(parts[1])
                
    print(res)