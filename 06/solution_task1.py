import sys

def string_to_int(list_of_strings: list) -> list:
    list_of_ints = []
    for s in list_of_strings:
        try:
            list_of_ints.append(int(s))
        except (TypeError, ValueError):
            continue
    return list_of_ints

def distance(speed, time):
    return speed * time

def options(max):
    return [distance(i, max - i) for i in range(1, max + 1)]

def ways_to_win(ms, record):
    option_list = options(ms)
    count = sum(1 for o in option_list if o > record)
    return count

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

times = string_to_int(lines[0].split(':')[1].strip().split())
distances = string_to_int(lines[1].split(':')[1].strip().split())

result = 1

for i in range(len(times)):
    result *= ways_to_win(times[i], distances[i])

print(result)



