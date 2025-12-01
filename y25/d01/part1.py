def answer(filename: str) -> int:
    with open(filename) as file:
        position = 50
        result = 0
        for line in file:
            line = line.strip()
            direction = line[0]
            distance = int(line[1:])

            movement = distance * (1 if direction == "R" else -1)

            position = (position + movement) % 100

            if position == 0:
                result += 1
    return result
