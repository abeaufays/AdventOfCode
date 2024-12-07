"""
This is a very inefficient implementation
"""

EMPTY = "."
OBSTACLE = "#"
DIRECTIONS = ["^", ">", "v", "<"]


def answer(map_: list[str]) -> int:
    result = 0
    start_position = find_start(map_)
    start_direction = read(map_, start_position)

    # write(map_, start_position, EMPTY)

    for line_idx, line in enumerate(map_):
        print(line_idx)
        for col_idx, content in enumerate(line):
            if content == EMPTY:  # remove start_position ?
                write(map_, (line_idx, col_idx), OBSTACLE)
                if is_looping(map_, start_position, start_direction):
                    result += 1
                write(map_, (line_idx, col_idx), EMPTY)

    return result


def is_looping(
    map_: list[str], start_position: tuple[int, int], start_direction: str
) -> bool:
    current_position = start_position
    current_direction = start_direction

    memory: list[tuple[int, int, str]] = []
    while True:
        next_positon = get_front_pos(current_direction, current_position)
        if is_position_out_of_map(map_, next_positon):
            return False
        elif (*current_position, current_direction) in memory:
            return True
        elif read(map_, next_positon) == OBSTACLE:
            current_direction = turn(current_direction)
        else:
            memory.append((*current_position, current_direction))
            current_position = next_positon


def read(map_: list[str], position: tuple[int, int]) -> str:
    return map_[position[0]][position[1]]


def write(map_: list[str], position: tuple[int, int], content: str) -> None:
    if len(content) != 1:
        raise ValueError
    map_[position[0]] = (
        map_[position[0]][: position[1]]
        + content
        + map_[position[0]][position[1] + 1 :]
    )


def is_position_out_of_map(map_: list[str], position: tuple[int, int]):
    return (not (0 <= position[0] < len(map_))) or (
        not (0 <= position[1] < len(map_[0]))
    )


def turn(current_direction: str) -> str:
    if current_direction not in DIRECTIONS:
        raise ValueError
    return DIRECTIONS[(DIRECTIONS.index(current_direction) + 1) % 4]


def find_start(map_: list[str]) -> tuple[int, int]:
    for idx, line in enumerate(map_):
        if "^" in line:
            return (idx, line.index("^"))
    raise ValueError


def get_front_pos(direction: str, position: tuple[int, int]) -> tuple[int, int]:
    direction_vector = {
        "^": (-1, 0),
        "v": (1, 0),
        ">": (0, 1),
        "<": (0, -1),
    }[direction]
    return (position[0] + direction_vector[0], position[1] + direction_vector[1])


def tests():
    map_ = [
        "....",
        "....",
        "..^.",
    ]
    write(map_, (1, 1), "X")
    assert map_ == [
        "....",
        ".X..",
        "..^.",
    ]

    assert turn("^") == ">"
    assert turn(">") == "v"
    assert turn("v") == "<"
    assert turn("<") == "^"

    assert is_position_out_of_map(map_, (-1, 1))
    assert is_position_out_of_map(map_, (3, 1))
    assert is_position_out_of_map(map_, (1, -2))
    assert is_position_out_of_map(map_, (1, 4))
    assert not is_position_out_of_map(map_, (1, 1))


def test_is_looping():
    looping_map = [
        ".#...",
        "....#",
        "#....",
        "...#.",
        ".....",
    ]
    assert is_looping(looping_map, (2, 1), "^")


tests()
test_is_looping()

with open("2024/6/test") as file:
    test_map = file.read().splitlines()
    assert (test_start_pos := find_start(test_map)) == (6, 4)
    assert get_front_pos("^", test_start_pos) == (5, 4)
    # assert not is_looping(test_map.copy())
    assert (result := answer(test_map)) == (
        expected := 6
    ), f"Test sample: {result} is not {expected}"

with open("2024/6/data") as file:
    map_ = file.read().splitlines()
    print(answer(map_))
