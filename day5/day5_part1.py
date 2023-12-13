import re

def conversion(query, mapping):
    for source, dest, length in mapping:  
        if source <= query <= source + length:
            return dest + (query - source)
    return query

with open("puzzle_input.txt", "r") as input_file:
    input_str = input_file.read()

    cur_values = map(int, re.match(r'^seeds:\s(.+)$', input_str, flags=re.MULTILINE).group(1).split(' '))
    
    map_names = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
    for name in map_names:
        map_lines = re.findall(rf"^{name}\smap:\s(.*?)\n$^$", input_str, flags=re.DOTALL|re.MULTILINE)[0].split('\n')

        mapping = [(int(source), int(dest), int(length)) for dest, source, length in (line.split() for line in map_lines)]
        cur_values = [conversion(n, mapping) for n in cur_values]
    
    print(min(cur_values))