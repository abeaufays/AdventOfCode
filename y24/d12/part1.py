import numpy as np
import typing

DIRECTIONS = [
    RIGHT := (0, 1),
    LEFT := (0, -1),
    DOWN := (1, 0),
    UP := (-1, 0),
]

type Position = tuple[int, int]


def answer(map_data: np.ndarray) -> int:
    non_visited: list[Position] = []
    result = 0
    for line_idx in range(len(map_data)):
        for col_idx in range(len(map_data[0])):
            non_visited.append((line_idx, col_idx))

    while non_visited:
        region_area = 0
        region_perimeter = 0
        current_position = non_visited.pop()
        current_region_to_visit: list[Position] = [current_position]
        while current_region_to_visit:
            current_position = current_region_to_visit.pop()
            region_area += 1
            for adjacent_position in (
                add(current_position, direction) for direction in DIRECTIONS
            ):
                if (
                    is_in_bound_of(adjacent_position, map_data)
                    and map_data[adjacent_position] == map_data[current_position]
                    and adjacent_position in non_visited
                ):
                    non_visited.remove(adjacent_position)
                    current_region_to_visit.append(adjacent_position)
                elif (
                    is_in_bound_of(adjacent_position, map_data)
                    and map_data[adjacent_position] != map_data[current_position]
                ) or not is_in_bound_of(adjacent_position, map_data):
                    region_perimeter += 1
        print(
            "Region ",
            map_data[current_position],
            ", Area ",
            region_area,
            ", Perimeter ",
            region_perimeter,
        )
        result += region_perimeter * region_area
    return result


def is_in_bound_of(position: Position, map_data: np.ndarray) -> bool:
    map_shape = map_data.shape
    return 0 <= position[0] <= map_shape[0] - 1 and 0 <= position[1] <= map_shape[1] - 1


def add(one: Position, other: Position) -> Position:
    return (one[0] + other[0], one[1] + other[1])


def to_ndarray(file: typing.TextIO) -> np.ndarray:
    return np.array([list(map(str, line.strip())) for line in file.readlines()])


def test(result, expected):
    assert result == expected, f"{result} is not {expected}"


def test_suite1():
    with open("2024/12/test1") as file:
        map_data = to_ndarray(file)
        test(answer(map_data), 140)


def test_suite2():
    with open("2024/12/test2") as file:
        map_data = to_ndarray(file)
        test(answer(map_data), 772)


def test_suite3():
    with open("2024/12/test3") as file:
        map_data = to_ndarray(file)
        test(answer(map_data), 1930)


test_suite1()
test_suite2()
test_suite3()

with open("2024/12/data") as file:
    map_data = to_ndarray(file)
    print(answer(map_data))
