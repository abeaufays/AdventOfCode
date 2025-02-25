from collections.abc import Sequence
import numpy as np
from utils.vec2d import Vec2D


def str_to_map(input: str) -> np.ndarray:
    return np.array([list(line.strip()) for line in input.splitlines()])


def to_str(map_data: np.ndarray) -> str:
    shape = map_data.shape
    result = ""
    for line_idx in range(shape[0]):
        for col_idx in range(shape[1]):
            result += map_data[(line_idx, col_idx)]
        result += "\n"
    return result


def get_position_of(map_data: np.ndarray, item) -> Vec2D:
    positions = np.where(map_data == item)
    return (positions[0][0], positions[1][0])


def is_position_in_map(position: Vec2D, map_data: np.ndarray) -> bool:
    return 0 <= position[0] < map_data.shape[0] and 0 <= position[1] < map_data.shape[1]


def print_with_highlighted(map_data: np.ndarray, highlighted: Sequence[Vec2D]):
    shape = map_data.shape
    result = ""
    for line_idx in range(shape[0]):
        for col_idx in range(shape[1]):
            if (line_idx, col_idx) in highlighted:
                result += "\033[93m" + str(map_data[(line_idx, col_idx)]) + "\033[0m"
            else:
                result += map_data[(line_idx, col_idx)]
        result += "\n"
    print(result)
