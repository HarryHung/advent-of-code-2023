import math

with open("puzzle_input.txt", "r") as input_file:
    lines = input_file.readlines()
    
    time = int(''.join(lines[0].split()[1:]))
    distance = int(''.join(lines[1].split()[1:]))

    # 1: travel_time = race_time - button_time
    # 2: travel_distance = travel_time * button_time
    # substituting 1 into 2
    # travel_distance = (race_time - button_time) * button_time
    # travel_distance = race_time * button_time - button_time ** 2
    # button_time ** 2 - race_time * button_time + travel_distance = 0
    # Use quadratic formula solve below

    b1 = (time + math.sqrt(time ** 2 - 4 * distance)) / 2
    b2 = (time - math.sqrt(time ** 2 - 4 * distance)) / 2

    print(math.ceil(b1) - math.floor(b2) - 1)