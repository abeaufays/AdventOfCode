from __future__ import annotations
import numpy as np

START = 0
END = 9


DIRECTIONS = [
    RIGHT := (0, 1),
    LEFT := (0, -1),
    DOWN := (1, 0),
    UP := (-1, 0),
]

type Position = tuple[int, int]


def add(one: Position, other: Position) -> Position:
    return (one[0] + other[0], one[1] + other[1])


def is_in_bound_of(position: Position, map_data: np.ndarray) -> bool:
    map_shape = map_data.shape
    return 0 <= position[0] <= map_shape[0] - 1 and 0 <= position[1] <= map_shape[1] - 1


def answer(map_data: np.ndarray) -> int:
    result = 0
    for start_position in find_start_positions(map_data):
        visited = list()
        next_node_to_lookup = [start_position]
        while next_node_to_lookup:
            current_node = next_node_to_lookup.pop()
            visited.append(current_node)

            if map_data[current_node] == END:
                result += 1
                continue

            for adjacent_position in (
                add(current_node, direction) for direction in DIRECTIONS
            ):
                if (
                    is_in_bound_of(adjacent_position, map_data)
                    and map_data[adjacent_position] == map_data[current_node] + 1
                    and adjacent_position not in visited
                ):
                    next_node_to_lookup.append(adjacent_position)

    return result


def find_start_positions(map_data: np.ndarray) -> list[Position]:
    result = []
    for line_idx, line in enumerate(map_data):
        for col_idx, content in enumerate(line):
            if content == START:
                result.append((line_idx, col_idx))
    return result


def test(result, expected):
    assert result == expected, f"{result} is not {expected}"


def test_suite_1():
    with open("2024/10/test") as file:
        map_data = np.array([list(map(int, line.strip())) for line in file.readlines()])
        test(
            find_start_positions(map_data),
            [
                (0, 2),
                (0, 4),
                (2, 4),
                (4, 6),
                (5, 2),
                (5, 5),
                (6, 0),
                (6, 6),
                (7, 1),
            ],
        )
        test(answer(map_data), 36)


test_suite_1()


with open("2024/10/data") as file:
    map_data = np.array([list(map(int, line.strip())) for line in file.readlines()])
    print(answer(map_data))
