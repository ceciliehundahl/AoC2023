"""
Warning: This script is in contest for the ugliest piece of code ever written.
It does the job, but proceed with caution.
"""

import numpy as np

with open('input.txt', 'r') as f:
    lines = f.readlines()

# get dimensions of engine schematic 

cols = 0

for line in lines:
    if len(line.strip()) > cols:
        cols = len(line.strip())

rows = len(lines)

# denote any part of the schematic that is adjacent to a symbol

symbol_map = np.zeros((rows,cols))

row = 0

for line in lines:
    col = 0
    for element in line.strip():
        if not element.isdigit() and element != ".":
#            print(f"{element}: ({row}, {col})")
            adjacent = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                        (row, col - 1), (row, col + 1),
                        (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
            for coordinate in adjacent:
                try:
                    symbol_map[coordinate[0], coordinate[1]] = 1
                except IndexError:
                    continue
        col += 1
    row += 1


# sum up digits adjacent to symbols

adjacent_sum = 0

row = 0

for line in lines:
    digit_str = ""
    start_coor = None
    end_coor = None

    col = 0
    for element in line:
        if element.isdigit():
            digit_str += element
            end_coor = col
            if start_coor is None:
                start_coor = col
        else:
            if start_coor is not None:
                adjacent = False
                for i in range(start_coor, end_coor + 1):
                    if symbol_map[row][i] > 0:
                        adjacent = True
                if adjacent:
                    adjacent_sum += int(digit_str)
                digit_str = ""
                start_coor = None
                end_coor = None
        col += 1
    row += 1

print(adjacent_sum)

