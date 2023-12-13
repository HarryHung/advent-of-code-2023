import re

with open("puzzle_input.txt", "r") as input_file:
    input_str = input_file.read()

    seed_pairs = list(map(int, re.match(r'^seeds:\s(.+)$', input_str, flags=re.MULTILINE).group(1).split(' ')))

    cur_ranges = [(seed_start, seed_start + length) for seed_start, length in zip(seed_pairs[::2], seed_pairs[1::2])]
    
    map_names = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
    for name in map_names:
        map_lines = re.findall(rf"^{name}\smap:\s(.*?)\n$^$", input_str, flags=re.DOTALL|re.MULTILINE)[0].split('\n')

        mapping = sorted([(int(source), int(dest), int(length)) for dest, source, length in (line.split() for line in map_lines)])

        next_ranges = []

        while len(cur_ranges) > 0:
            start, end = cur_ranges.pop()
            for source, dest, length in mapping:
                diff = dest - source

                if source <= start < source + length:
                    if end < source + length:
                        next_ranges.append((start + diff, end + diff))
                    else:
                        next_ranges.append((start + diff, dest + length))
                        cur_ranges.append((source + length, end))
                    break
            else:
                next_ranges.append((start, end))

        cur_ranges = next_ranges

        
print(sorted(cur_ranges)[0][0])    
