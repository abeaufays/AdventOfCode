def answer(filename: str) -> int:
    with open(filename) as file:
        position = 50
        result = 0
        for line in file:
            line = line.strip()
            direction = line[0]
            distance = int(line[1:])

            movement = distance * (1 if direction == "R" else -1)

            if abs(movement) >= 100:
                number_of_turns = int(movement / 100)
                movement = movement - (100 * number_of_turns)
                result += abs(number_of_turns)

            unresolved_next_position = position + movement
            if position != 0 and (
                unresolved_next_position <= 0 or 100 <= unresolved_next_position
            ):
                result += 1

            position = unresolved_next_position % 100

    return result
