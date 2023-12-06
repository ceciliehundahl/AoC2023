import sys

def string_to_int(string: str) -> list:
    return [int(s) for s in string.split()]
    
def read_seed(line):
    return string_to_int(line.split(':')[1].strip())

def map(segment):
    list_of_tuples = []
    for line in segment[1:]:
        # destination range start, the source range start, and the range length.
        (dest_start, source_start, range_len) = string_to_int(line)
        list_of_tuples.append((dest_start, source_start, range_len))
    return list_of_tuples

def lookup(source, map):
    for (dest_start, source_start, range_len) in map:
        rel_location = source - source_start
        if rel_location >= 0 and rel_location < range_len:
            return dest_start + rel_location
    return source

try:
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
except FileNotFoundError:
    lines = [sys.argv[1]]
except IndexError:
    print("Supply argument specifying input file or a string to test on")
    sys.exit()

seeds = read_seed(lines[0])

print(seeds)

list_of_maps = []

segment = []

for line in lines[1:]:
    if len(line) > 1:
        segment.append(line)
    else:
        if len(segment) > 0:
            list_of_maps.append(map(segment))
        segment = []

list_of_maps.append(map(segment))

# work it through

final_locations = {}

for seed in seeds:
    temp = seed
    for map in list_of_maps:
        temp = lookup(temp, map)
    final_locations[temp] = seed

minimum = min(final_locations)

print(minimum)

