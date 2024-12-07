OBSTACLE = "#"
POSITIONS = ["^", ">", "v", "<"]


def answer(map_: list[str]) -> int:
    current_position = find_start(map_)

    while True:
        next_positon = get_front_pos(read(map_, current_position), current_position)
        if is_position_out_of_map(map_, next_positon):
            return sum(line.count("X") for line in map_) + 1
        elif read(map_, next_positon) == OBSTACLE:
            turn(map_, current_position)
        else:
            current_direction = read(map_, current_position)
            write(map_, current_position, "X")
            write(map_, next_positon, current_direction)
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


def turn(map_: list[str], position: tuple[int, int]) -> None:
    if (current_direction := read(map_, position)) not in POSITIONS:
        raise ValueError
    write(map_, position, POSITIONS[(POSITIONS.index(current_direction) + 1) % 4])


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

    turn(map_, (2, 2))
    assert map_ == [
        "....",
        ".X..",
        "..>.",
    ]
    assert is_position_out_of_map(map_, (-1, 1))
    assert is_position_out_of_map(map_, (3, 1))
    assert is_position_out_of_map(map_, (1, -2))
    assert is_position_out_of_map(map_, (1, 4))
    assert not is_position_out_of_map(map_, (1, 1))


tests()


with open("2024/6/test") as file:
    test_map = file.read().splitlines()
    assert (test_start_pos := find_start(test_map)) == (6, 4)
    assert get_front_pos("^", test_start_pos) == (5, 4)
    assert (result := answer(test_map)) == (
        expected := 41
    ), f"Test sample: {result} is not {expected}"

with open("2024/6/data") as file:
    map_ = file.read().splitlines()
    print(answer(map_))
