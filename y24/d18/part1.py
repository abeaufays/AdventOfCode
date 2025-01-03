from dataclasses import dataclass
from sortedcontainers import SortedKeyList

import sys
import numpy as np

from utils import maps, vec2d

SAFE = "."
CORRUPTED = "#"


DIRECTIONS = [
    UP := (-1, 0),
    RIGHT := (0, 1),
    DOWN := (1, 0),
    LEFT := (0, -1),
]


@dataclass
class State:
    position: vec2d.Vec2D
    lenght: int


class Context:
    def __init__(self, map_data: np.ndarray, end: vec2d.Vec2D):
        self.map_data = map_data
        self.position_memory = np.full(map_data.shape, sys.maxsize)
        self.end = end


def next_states(current_state: State, context: Context) -> list[State]:
    result = []
    for direction in DIRECTIONS:
        following_position = vec2d.add(current_state.position, direction)
        if (
            not maps.is_position_in_map(following_position, context.map_data)
            or context.map_data[following_position] == CORRUPTED
        ):
            continue

        new_state = State(following_position, current_state.lenght + 1)
        if context.position_memory[new_state.position] > new_state.lenght:
            context.position_memory[new_state.position] = new_state.lenght
            result.append(new_state)

    return result


def answer(filename: str) -> int:
    with open(filename) as file:
        lines = file.read().splitlines()
        shape_raw = tuple(map(int, lines[0].split(",")))
        shape = (shape_raw[0], shape_raw[1])
        bytes_to_take = int(lines[1])

        start = (0, 0)
        end = vec2d.add(shape, (-1, -1))

        map_data = np.full(shape, SAFE)
        for corrupted in lines[3 : (bytes_to_take + 3)]:
            coord = tuple(map(int, corrupted.split(",")))
            map_data[coord] = CORRUPTED
        context = Context(map_data, end)

    search = SortedKeyList([State(start, 0)], lambda x: x.lenght)
    i = 0
    while search:
        i += 1
        state = search.pop(0)
        if state.position == end:
            return state.lenght
        else:
            search.update(next_states(state, context))

    return 0


# print(answer("y24/d18/data"))
