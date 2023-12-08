with open("puzzle_input.txt", "r") as input_file:
    sum = 0

    for line in input_file:
        num_list = [str(x) for x in line if x.isdecimal()]
        sum += int(num_list[0] + num_list[-1])

    print(sum)