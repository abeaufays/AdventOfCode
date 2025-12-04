from typing import Generator
from utils import maps, vec2d
import numpy as np

ADJACENT_POSITIONS_DELTA = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)


def adjacent_position_generator(
    position: vec2d.Vec2D, map_data: np.ndarray
) -> Generator[vec2d.Vec2D, None, None]:
    for adjacent_position_delta in ADJACENT_POSITIONS_DELTA:
        adjacent_position = vec2d.add(position, adjacent_position_delta)
        if maps.is_position_in_map(adjacent_position, map_data):
            yield adjacent_position


def is_roll_removable(position: tuple[int, int], map_data: np.ndarray) -> bool:
    count = 0
    for adjacent_position in adjacent_position_generator(position, map_data):
        if map_data[adjacent_position] == "@":
            count += 1
            if count == 4:
                return False
    return True


def answer(filename: str) -> int:
    result = 0
    debug_list = []
    to_evaluate = []
    with open(filename) as file:
        map_data = maps.str_to_map(file.read())
        map_shape = map_data.shape
        for line_idx in range(map_shape[0]):
            for col_idx in range(map_shape[1]):
                position = (line_idx, col_idx)
                if map_data[position] == "@":
                    to_evaluate.append(position)

        while to_evaluate:
            position = to_evaluate.pop()
            if map_data[position] == "@" and is_roll_removable(position, map_data):
                result += 1
                map_data[position] = "."
                debug_list.append(position)
                for adjacent_position in adjacent_position_generator(
                    position, map_data
                ):
                    if map_data[adjacent_position] == "@":
                        to_evaluate.append(adjacent_position)

    maps.print_with_highlighted(map_data, debug_list)
    return result
