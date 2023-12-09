import numpy as np
import sys

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

def all_zeros(list):
    for x in list:
        if x != 0:
            return False
    return True

before_sum = after_sum = 0

for line in lines:
    predictions = [[int(x) for x in line.split(' ')]]

    # map out
    while not all_zeros(predictions[-1]): 
        new = np.diff(predictions[-1])
        predictions.append(new)

    # go back
    before = after = 0
    for pred in predictions[::-1]:
        after += pred[-1]
        before = pred[0] - before

    before_sum += before
    after_sum += after

print(after_sum)
print(before_sum)
