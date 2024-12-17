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
        region_borders: list[tuple[Position, Position]] = []
        current_position = non_visited.pop()
        current_region_to_visit: list[Position] = [current_position]
        while current_region_to_visit:
            current_position = current_region_to_visit.pop()
            region_area += 1
            for direction in DIRECTIONS:
                adjacent_position = add(current_position, direction)
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
                    region_borders.append((current_position, direction))

        border_segments: list[list[tuple[Position, Position]]] = []
        while region_borders:
            current_border = region_borders.pop()
            adjacent_segment: list[list[tuple[Position, Position]]] = (
                get_adjacent_border_segments(border_segments, current_border)
            )
            if len(adjacent_segment) == 2:
                border_segments.append(
                    adjacent_segment[0] + adjacent_segment[1] + [current_border]
                )
                border_segments.remove(adjacent_segment[0])
                border_segments.remove(adjacent_segment[1])
            elif len(adjacent_segment) == 1:
                adjacent_segment[0].append(current_border)
            else:
                border_segments.append([current_border])
        region_perimeter = len(border_segments)
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


def get_adjacent_border_segments(
    border_segments: list[list[tuple[Position, Position]]],
    current_border: tuple[Position, Position],
) -> list[list[tuple[Position, Position]]]:
    result = []
    for segment in border_segments:
        if any(
            are_adjacent_border(current_border, border_in_segment)
            for border_in_segment in segment
        ):
            result.append(segment)
    return result


def is_in_bound_of(position: Position, map_data: np.ndarray) -> bool:
    map_shape = map_data.shape
    return 0 <= position[0] <= map_shape[0] - 1 and 0 <= position[1] <= map_shape[1] - 1


def are_adjacent_border(
    a: tuple[Position, Position], b: tuple[Position, Position]
) -> bool:
    return a[1] == b[1] and are_adjacent(a[0], b[0])


def are_adjacent(a: Position, b: Position) -> bool:
    return (a[0] - b[0] == 0 and abs(a[1] - b[1]) == 1) or (
        abs(a[0] - b[0]) == 1 and a[1] - b[1] == 0
    )


def add(one: Position, other: Position) -> Position:
    return (one[0] + other[0], one[1] + other[1])


def to_ndarray(file: typing.TextIO) -> np.ndarray:
    return np.array([list(map(str, line.strip())) for line in file.readlines()])


def test(result, expected):
    assert result == expected, f"{result} is not {expected}"


def test_suite1():
    with open("2024/12/test1") as file:
        map_data = to_ndarray(file)
        test(answer(map_data), 80)


def test_suite2():
    with open("2024/12/test2") as file:
        map_data = to_ndarray(file)
        test(answer(map_data), 436)


def test_suite3():
    with open("2024/12/test3") as file:
        map_data = to_ndarray(file)
        test(answer(map_data), 1206)


def test_suite4():
    with open("2024/12/test4") as file:
        map_data = to_ndarray(file)
        test(answer(map_data), 236)


def test_are_adjacent():
    assert not are_adjacent((1, 1), (1, 1))
    assert not are_adjacent((1, 1), (2, 2))
    assert not are_adjacent((1, 1), (-1, -1))
    assert are_adjacent((1, 1), (1, 2))
    assert are_adjacent((1, 1), (0, 1))
    assert are_adjacent((1, 0), (1, 1))


test_are_adjacent()

test_suite1()
test_suite2()
test_suite4()
test_suite3()

with open("2024/12/data") as file:
    map_data = to_ndarray(file)
    print(answer(map_data))
