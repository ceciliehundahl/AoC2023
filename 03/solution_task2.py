with open('input.txt', 'r') as f:
    lines = f.readlines()

cols = 0

for line in lines:
    if len(line.strip()) > cols:
        cols = len(line.strip())

rows = len(lines)

print(f"Dimensions: {rows}, {cols}")

gear_ratio_sum = 0

for i in range(rows):
    for j in range (cols):
        if lines[i][j] == "*":
            adjacent = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                        (i, j - 1), (i, j + 1),
                        (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
            adjacent_digits = []
            for coordinate in adjacent:
                try:
                    if lines[coordinate[0]][coordinate[1]].isdigit():
                        adjacent_digits.append(coordinate)
                except IndexError:
                    continue
            if len(adjacent_digits) > 1:
                covered = set()
                digits = []
                for coordinate in adjacent_digits:
                    if coordinate not in covered:
                        start = coordinate[1]
                        while start > 0 and lines[coordinate[0]][start - 1].isdigit():
                            start -= 1
                        end = coordinate[1]
                        while end < cols and lines[coordinate[0]][end + 1].isdigit():
                            end += 1
                        for x in range(start, end + 1):
                            covered.add((coordinate[0], x))
                        digits.append(int(lines[coordinate[0]][start : end + 1]))
                if len(digits) == 2:
                    gear_ratio_sum += digits[0] * digits[1]


print(gear_ratio_sum)
