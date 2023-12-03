digits = {'one': 1,
          'two': 2,
          'three': 3,
          'four': 4,
          'five' : 5,
          'six' : 6,
          'seven' : 7,
          'eight' : 8,
          'nine' : 9
          }

def parse_digits(line: str) -> int:
    """
    Crude parsing from the strings to digits. The text is not deleted, the digit
    is just inserted; It's not pretty, but it works.
    """
    parsed = ""
    remaining = line
    while len(remaining) > 0:
        for d in digits:
            if remaining.startswith(d):
                parsed += str(digits[d])
        parsed += remaining[0]
        remaining = remaining [1:]
    return parsed

def get_calibation_value(line: str) -> int:
    """
    On each line, the calibration value can be found by combining the first
    digit and the last digit (in that order) to form a single two-digit number.
    """
    first = None
    last = None
    for element in line:
        try:
            number = int(element)
        except (TypeError, ValueError):
            continue
        if not first:
            first = number
            last = number
        else:
            last = number
    if first and last:
        return (first*10 + last)
    else:
        return 0

with open("input.txt", "r") as f:
    lines = f.readlines()

# TASK 1

calibration_sum = 0

for line in lines:
    value = get_calibation_value(line)
    calibration_sum += value
#    print(f"{line}: {value}")

print(calibration_sum)

# TASK 2

calibration_sum = 0

for line in lines:
    parsed = parse_digits(line)
    value = get_calibation_value(parsed)
    calibration_sum += value

print(calibration_sum)

