not_symbol = set([*map(str, range(10)), '.', '\n'])
directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

with open("puzzle_input.txt", "r") as input_file:
    content = input_file.read().splitlines()

    res = 0

    for i, line in enumerate(content):
        cache = []
        part = False

        for j, char in enumerate(line):
            if char.isdigit():
                cache.append(char)
                if any (0 <= (i_check := i + di) < len(content) and 0 <= (j_check := j + dj) < len(line) and content[i_check][j_check] not in not_symbol for di, dj in directions):
                    part = True
            
            if not char.isdigit() or j == len(line) - 1:
                if part:
                    res += int(''.join(cache))
                cache = []
                part = False


    print(res)