import json
import os

dirname = os.path.dirname(os.path.realpath(__file__)) + "/"
filename = dirname + "data.txt"

RED = "red"
GREEN = "green"
BLUE = "blue"
colors = [RED, GREEN, BLUE]


question = {RED: 12, GREEN: 13, BLUE: 14}


result_part1 = 0
result = 0
with open(filename, "r") as file:
    data = json.load(file)

    for game in data:
        maxs = {RED: 0, GREEN: 0, BLUE: 0}
        for tirage in game["tirages"]:
            for color in colors:
                maxs[color] = max(tirage.get(color, 0), maxs[color])

        if all(maxs[color] <= question.get(color, 0) for color in colors):
            result_part1 += game["id"]
        power = maxs[RED] * maxs[GREEN] * maxs[BLUE]
        print(
            f"Game {game['id']} : {', '.join([color + ' ' + str(maxs[color]) for color in colors])} / power : {power}"
        )
        result += power

print(result_part1)
print(result)
