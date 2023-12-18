with open("puzzle_input.txt", "r") as input_file:
    lines = input_file.readlines()
    
    time = int(''.join(lines[0].split()[1:]))
    distance = int(''.join(lines[1].split()[1:]))

    res = 0
    for t in range(1, time + 1):
        if (time - t) * t > distance:
            res += 1

    print(res)