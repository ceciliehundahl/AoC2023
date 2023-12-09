import math
import sys

INSTRUCTIONS = "LRRLRRLRRLRRRLRRLRRRLRRLRRRLRLRLLRLRLRRLLLRLRLRRRLRRLRLRRRLRRLRRLRRLLLRRLRRRLRRRLRLLRRLRLLRRLRRRLRRLRLRRRLRLRLRRLRLRRRLLRRRLLRRRLRLRRRLRRLLRRLRRRLRRLRRLLRRLRRLRRRLLLRRRLRRLRRLRRLRLRRRLRRLLLLRLRRLRRRLRLLRRLRLLRRLRRRLRRRLRRRLLRRLRRLRRLRRRLRRLRRRLLRLRRRLRRRLRRRLLRRRLRRLRRRR"

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

MAP = {}

for line in lines:
    key = line.split('=')[0].strip()
    LL, RR = line.split('=')[1].replace('(', '').replace(')', '').split(',')
    LL, RR = LL.strip(), RR.strip()
    MAP[key] = (LL, RR)

starts = []

for node in MAP:
    if node[2] == 'A':
        starts.append(node)

print(starts)
scores = []

for x in range(len(starts)):
    cont = True
    i = 0
    count = 0
    current = starts[x]

    while cont:
        if i >= len(INSTRUCTIONS):
            i = 0
        ins = INSTRUCTIONS[i]
        if ins == 'L':
            current = MAP[current][0]
        elif ins == 'R':
            current = MAP[current][1]
        count += 1
        if current[2] == 'Z':
            cont = False
        i += 1
    scores.append(count)

print(math.lcm(*scores))

