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

cont = True
i = 0
current = 'AAA'
count = 0

while cont:
    if i >= len(INSTRUCTIONS):
        i = 0
    ins = INSTRUCTIONS[i]
    if ins == 'L':
        current = MAP[current][0]
    elif ins == 'R':
        current = MAP[current][1]
    count += 1
    if current == 'ZZZ':
        cont = False
    else:
        i += 1

print(count)



