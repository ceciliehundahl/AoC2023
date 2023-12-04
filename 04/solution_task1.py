def string_to_int(set_of_strings: set) -> set:
    set_of_ints = set()
    for s in set_of_strings:
        try:
            set_of_ints.add(int(s))
        except (TypeError, ValueError):
            continue
    return set_of_ints

def extract_numbers(line: str) -> tuple:
    winning = string_to_int(set(line.split(':')[1].split('|')[0].split(' ')))
    mine = string_to_int(set(line.split(':')[1].split('|')[1].split(' ')))
    return (winning, mine)

def get_score(winning: set, mine: set) -> int:
    score = 0
    for no in mine:
        if no in winning:
            if score == 0:
                score += 1
            else:
                score *= 2
    return score

with open('input.txt', 'r') as f:
    lines = f.readlines()

points = 0

for line in lines:
    winning, mine = extract_numbers(line)
    points += get_score(winning, mine)

print(points)