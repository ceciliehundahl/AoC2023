def string_to_int(set_of_strings: set) -> set:
    set_of_ints = set()
    for s in set_of_strings:
        try:
            set_of_ints.add(int(s))
        except (TypeError, ValueError):
            continue
    return set_of_ints

def extract_numbers(line: str) -> tuple:
    card_id = int(line.split(':')[0][5:])
    winning = string_to_int(set(line.split(':')[1].split('|')[0].split(' ')))
    mine = string_to_int(set(line.split(':')[1].split('|')[1].split(' ')))
    return (card_id, winning, mine)

def get_correct(winning: set, mine: set) -> int:
    correct = 0
    for no in mine:
        if no in winning:
            correct += 1
    return correct

with open('input.txt', 'r') as f:
    lines = f.readlines()

cards = {}

for line in lines:
    card_id, winning, mine = extract_numbers(line)
    if card_id in cards:
        cards[card_id] += 1
    else:
        cards[card_id] = 1
    copies = cards[card_id]

    correct = get_correct(winning, mine)
    next_card = card_id + 1

    for card in range(next_card, next_card + correct):
        if card in cards:
            cards[card] += copies
        else:
            cards[card] = copies


print(sum(cards.values()))

