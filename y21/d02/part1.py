def answer(filename: str) -> int:
    horizontal_position: int = 0
    depth: int = 0
    with open(filename) as file:
        for line in file:
            match line.split():
                case ["down", speed] if speed.isdigit():
                    depth += int(speed)
                case ["up", speed] if speed.isdigit():
                    depth -= int(speed)
                case ["forward", speed] if speed.isdigit():
                    horizontal_position += int(speed)
                case _:
                    raise ValueError(line)

    return horizontal_position * depth  # 1815044
