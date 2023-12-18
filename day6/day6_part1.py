import math

with open("puzzle_input.txt", "r") as input_file:
    lines = input_file.readlines()
    
    res = []

    for time, distance in zip(map(int, lines[0].split()[1:]), map(int, lines[1].split()[1:])):
        cur = 0
        for t in range(1, time + 1):
            if (time - t) * t > distance:
                cur += 1
        res.append(cur)

    print(math.prod(res))