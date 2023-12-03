def power_of_min(game: str) -> int:
    """
    Returns lowest possible values for each color multiplied together
    """
    min_values = {'red': 0,
                  'green': 0,
                  'blue': 0
                  }
    sets = game.split(':')[1].split(';')
    for s in sets:
        result = s.split(',')
        for r in result:
            r = r.strip()
            value = int(r.split(' ')[0])
            color = r.split(' ')[1]
            if value > min_values[color]:
                min_values[color] = value
    return min_values['red']*min_values['green']*min_values['blue']

with open("input.txt", "r") as f:
    lines = f.readlines()

power_sum = 0

for game in lines:
    power_sum += power_of_min(game)

print(power_sum)