import sys

def string_to_int(string: str) -> list:
    return [int(s) for s in string.split()]

def string_to_seed_ranges(string: str) -> list:
    list_of_ints = [int(s) for s in string.split()]
    list_of_pairs = []
    for i in range(0, len(list_of_ints), 2):
        list_of_pairs.append((list_of_ints[i], list_of_ints[i+1]))
    return list_of_pairs

def read_seed(line):
    return string_to_seed_ranges(line.split(':')[1].strip())

def map(segment):
    list_of_tuples = []
    for line in segment[1:]:
        # destination range start, the source range start, and the range length.
        (dest_start, source_start, range_len) = string_to_int(line.strip())
        list_of_tuples.append((dest_start, source_start, range_len))
    return list_of_tuples

def range_lookup(list_of_ranges, map):
    lookup = list_of_ranges
    list_of_mapped_ranges = []
    while len(lookup) > 0:
        (target_start, target_range) = lookup.pop(0)
        mapped = False
        for (dest_start, source_start, range_len) in map:
            if not target_start:
                break
            # if all of target is within source
            if target_start >= source_start and target_start + target_range <= source_start + range_len:
                relative_location = target_start - source_start
                list_of_mapped_ranges.append((dest_start + relative_location, target_range))
                mapped = True
                break
            # if start of target is within source
            elif source_start <= target_start < (source_start + range_len):
                relative_location = target_start - source_start
                covered_range = range_len - relative_location
                list_of_mapped_ranges.append((dest_start + relative_location, covered_range))
                lookup.append(((target_start + covered_range), target_range - covered_range))
                mapped = True
                break
            # if end of target is within source
            elif source_start > (target_start + target_range) >= source_start:
                covered_range = target_start + target_range - source_start
                list_of_mapped_ranges.append((dest_start, covered_range))
                lookup.append((target_start, target_range - covered_range))
                mapped = True
                break
            # if target overlaps, but is wider than source
            elif target_start < source_start and (target_start + target_range) > (source_start + range_len):
                list_of_mapped_ranges.append((dest_start, range_len))
                lookup.append((target_start, source_start - target_start))
                lookup.append((source_start + range_len + 1, (target_start + target_range) - (source_start + range_len)))
                mapped = True
                break
        # if not found
        if not mapped:
            list_of_mapped_ranges.append((target_start, target_range))
    return list_of_mapped_ranges

try:
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
except FileNotFoundError:
    lines = [sys.argv[1]]
except IndexError:
    print("Supply argument specifying input file or a string to test on")
    sys.exit()

seeds = read_seed(lines[0])

list_of_maps = []

segment = []

for line in lines[1:]:
    if len(line) > 1:
        segment.append(line)
    else:
        if len(segment) > 0:
            list_of_maps.append(map(segment))
        segment = []


temp = seeds

for map in list_of_maps:
    temp = range_lookup(temp, map)

min = sys.maxsize

for (start, length) in temp:
    if start < min:
        min = start

print(min)



