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
    def __init__(self, map_shape: vec2d.Vec2D, corrupted_positions: list[vec2d.Vec2D]):
        self.corrupted_position = corrupted_positions
        self.pathing_memory = np.full(map_shape, sys.maxsize)
        self.start = (0, 0)
        self.end = vec2d.add(map_shape, (-1, -1))


def next_states(current_state: State, context: Context) -> list[State]:
    result = []
    for direction in DIRECTIONS:
        following_position = vec2d.add(current_state.position, direction)
        if (
            not maps.is_position_in_map(following_position, context.pathing_memory)
            or following_position in context.corrupted_position
        ):
            continue

        new_state = State(following_position, current_state.lenght + 1)
        if context.pathing_memory[new_state.position] > new_state.lenght:
            context.pathing_memory[new_state.position] = new_state.lenght
            result.append(new_state)

    return result


def is_end_reachable(context: Context) -> bool:
    search = SortedKeyList([State(context.start, 0)], lambda x: x.lenght)
    i = 0
    while search:
        i += 1
        state = search.pop(0)
        if state.position == context.end:
            return True
        else:
            search.update(next_states(state, context))
    return False


def answer(filename: str) -> vec2d.Vec2D:
    with open(filename) as file:
        lines = file.read().splitlines()
        shape_raw = tuple(map(int, lines[0].split(",")))
        known_reachable_end = int(lines[1])
        corrupted_positions = list(  # Convert list of string position to list of vec2d
            map(lambda x: ((t := tuple(map(int, x.split(","))))[0], t[1]), lines[3:])
        )
        shape = (shape_raw[0], shape_raw[1])

        search_lower_bound = known_reachable_end
        search_upper_bound = len(corrupted_positions)

        while search_upper_bound - search_lower_bound > 1:
            middle = (search_lower_bound + search_upper_bound) // 2

            context = Context(shape, corrupted_positions[:middle])
            if b := is_end_reachable(context):
                search_lower_bound = middle
            else:
                search_upper_bound = middle

    return corrupted_positions[search_lower_bound]


# print(answer("y24/d18/data"))
