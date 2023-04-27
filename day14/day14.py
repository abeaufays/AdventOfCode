file = open("day14/data.txt", "r")

width = 100
height = 170

# width = 16
# height = 14

assert width % 2 == 0

start_position = [0, width//2]

data = [["." for _ in range(width)] for _ in range(height+2)]

data[start_position[0]][start_position[1]] = "X"

for line in file:
    coords = map(lambda x: [*map(int, x.split(","))], line.split(" -> "))
    coords = [*map(lambda x: [x[0]-500 + width//2, x[1]], coords)]
    for i in range(len(coords)-1):
        for dx in range(min(coords[i][0], coords[i+1][0]), max(coords[i][0], coords[i+1][0]) + 1):
            for dy in range(min(coords[i][1], coords[i+1][1]), max(coords[i][1], coords[i+1][1]) + 1):
                data[dy][dx] = "#"


def can_spawn():
    global data
    global start_position
    return data[start_position[0]][start_position[1]] != "X"


def can_move(sandgrain):
    global data
    return data[sandgrain[0] + 1][sandgrain[1]] == "." or data[sandgrain[0] + 1][sandgrain[1] - 1] == "." or data[sandgrain[0] + 1][sandgrain[1] + 1] == "."


last_sandgrain_fell = False
count = 0


while can_spawn() or not last_sandgrain_fell:
    sand_grain_position = start_position.copy()
    count += 1
    while can_move(sand_grain_position) and sand_grain_position[0] < height:

        if data[sand_grain_position[0] + 1][sand_grain_position[1]] == ".":
            sand_grain_position = [
                sand_grain_position[0] + 1, sand_grain_position[1]]
        elif data[sand_grain_position[0] + 1][sand_grain_position[1] - 1] == ".":
            sand_grain_position = [
                sand_grain_position[0] + 1, sand_grain_position[1] - 1]
        elif data[sand_grain_position[0] + 1][sand_grain_position[1] + 1] == ".":
            sand_grain_position = [
                sand_grain_position[0] + 1, sand_grain_position[1] + 1]

    if sand_grain_position[0] >= height:
        last_sandgrain_fell = True
        count -= 1
    else:
        data[sand_grain_position[0]][sand_grain_position[1]] = "o"

    # [print("".join(x)) for x in data]

[print("".join(x)) for x in data]
print(count)
