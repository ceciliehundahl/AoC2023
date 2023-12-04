import sys

try:
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
except FileNotFoundError:
    lines = [sys.argv[1]]
except IndexError:
    print("Supply argument specifying input file or a string to test on")
    sys.exit()

for line in lines:
    print(line)
