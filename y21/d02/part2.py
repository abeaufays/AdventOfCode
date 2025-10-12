def answer(filename: str) -> int:
    horizontal_position: int = 0
    depth: int = 0
    aim: int = 0
    with open(filename) as file:
        for line in file:
            print(horizontal_position, depth, aim)
            match line.split():
                case ["down", amount] if amount.isdigit():
                    aim += int(amount)
                case ["up", amount] if amount.isdigit():
                    aim -= int(amount)
                case ["forward", amount] if amount.isdigit():
                    horizontal_position += int(amount)
                    depth += aim * int(amount)
                case _:
                    raise ValueError(line)

    return horizontal_position * depth  # 1815044
