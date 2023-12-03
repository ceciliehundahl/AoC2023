MAX_VALUES = {'red': 12,
              'green': 13,
              'blue': 14
              }

def validate_game(game: str) -> int:
    """
    Returns game ID if game is possible, returns 0 otherwise
    """
    sets = game.split(':')[1].split(';')
    for s in sets:
        result = s.split(',')
        for r in result:
            r = r.strip()
            value = int(r.split(' ')[0])
            color = r.split(' ')[1]
            if value > MAX_VALUES[color]:
                return 0
    return int(game.split(':')[0][5:])

with open("input.txt", "r") as f:
    lines = f.readlines()

id_sum = 0

for game in lines:
    id_sum += (validate_game(game))

print(id_sum)