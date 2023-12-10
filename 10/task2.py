import sys

with open(sys.argv[1], 'r') as f:
    MAP = f.readlines()

for r, line in enumerate(MAP):
    for c, element in enumerate(line):
        if element == 'S':
            S = (r, c)

PIPES = {'-': ((0, -1), (0, 1)),
         '|': ((-1, 0), (1, 0)),
         'L': ((-1, 0), (0, 1)),
         'J': ((0, -1), (-1, 0)),
         '7': ((1, 0), (0, -1)),
         'F': ((1, 0), (0, 1))
         }

def add_coords(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])

def move(standing_on, coming_from): # (r, c)
    r, c = standing_on
    # find which way to move
    symbol = MAP[r][c]
    option1, option2 = PIPES[symbol]
    # choose coordinate
    if add_coords(standing_on, option1) == coming_from:
        return add_coords(standing_on, option2)
    elif add_coords(standing_on, option2) == coming_from:
        return add_coords(standing_on, option1)
    else:
        print(f"Problem at {standing_on} with symbol {symbol}")

# find first move
def find_first(S):
    for path in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        candidate = add_coords(S, path)
        symbol = MAP[candidate[0]][candidate[1]]
        if symbol == '.':
            continue
        option1, option2 = PIPES[symbol]
        if add_coords(candidate, option1) == S:
            return candidate
        if add_coords(candidate, option2) == S:
            return candidate

new_map = []

for i in range(len(MAP)):
    inner = []
    for j in range(len(MAP[0])):
        inner.append(' ')
    inner.append(' ') # extra padding
    new_map.append(inner)
new_map.append(inner) # extra padding

pi, pj = S
i, j = find_first(S)

new_map[pi][pj] = 'x'
new_map[i][j] = 'x'

count = 1

while MAP[i][j] != 'S':
    ni, nj = move((i, j), (pi, pj))
    pi, pj = i, j
    i, j = ni, nj
    new_map[i][j] = 'x'
    count += 1

# we now have a map where the pipes are marked.
# going for marking what is OUTSIDE the pipes

def check_field(c1, c2):
    if c1 < 0 or c1 >= len(new_map) -1 or c1 < 0 or c2 >= len(new_map[0]) - 1:
        return
    if new_map[c1][c2] == 'x' or new_map[c1][c2] == '.':
        return
    else:
        new_map[c1][c2] = '.'
        check_field(c1 + 1, c2)
        check_field(c1, c2 + 1)

def check_field2(c1, c2): # another direction
    if c1 < 0 or c1 >= len(new_map) -1 or c1 < 0 or c2 >= len(new_map[0]) - 1:
        return
    if new_map[c1][c2] == 'x':
        return
    else:
        new_map[c1][c2] = 'm'
        check_field(c1 - 1, c2)
        check_field(c1, c2 - 1)

check_field(0,0)
check_field2(len(new_map) - 2, len(new_map[0]) - 2)

new_map[len(new_map) - 2][len(new_map[0]) - 2] = 'S'


for line in new_map:
    print(*line)
