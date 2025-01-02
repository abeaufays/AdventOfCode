from dataclasses import dataclass

import numpy as np
from utils import maps, vec2d
from y24.d16 import part1

START = "S"
END = "E"
WALL = "#"
EMPTY = "."

DIRECTIONS = [
    UP := (-1, 0),
    RIGHT := (0, 1),
    DOWN := (1, 0),
    LEFT := (0, -1),
]


@dataclass
class State:
    score: int
    direction: vec2d.Vec2D
    path: list[vec2d.Vec2D]

    @property
    def position(self) -> vec2d.Vec2D:
        return self.path[-1]


class Context:
    def __init__(self, map_data: np.ndarray, best_possible_score: int):
        self.map_data = map_data
        self.score_memory: dict[tuple[vec2d.Vec2D, vec2d.Vec2D], int] = dict()
        self.best_possible_score = best_possible_score


def next_states(current_state: State, context: Context) -> list[State]:
    current_direction_idx = DIRECTIONS.index(current_state.direction)
    result = []
    global counter

    for add_score, direction in (
        (1, current_state.direction),
        (1001, DIRECTIONS[(current_direction_idx + 1) % 4]),
        (1001, DIRECTIONS[(current_direction_idx - 1) % 4]),
    ):
        following_position = vec2d.add(current_state.position, direction)
        if (
            following_position in current_state.path
            or context.map_data[following_position] == WALL
        ):
            continue

        next_state = State(
            score=current_state.score + add_score,
            direction=direction,
            path=current_state.path + [following_position],
        )

        if next_state.score <= context.best_possible_score and (
            context.score_memory.get((next_state.position, next_state.direction))
            is None
            or next_state.score
            <= context.score_memory[(next_state.position, next_state.direction)]
        ):
            context.score_memory[(next_state.position, next_state.direction)] = (
                next_state.score
            )
            result.append(next_state)

    return result


def answer(filename: str) -> int:
    if "data" not in filename:
        best_possible_score = part1.answer(filename)
    else:
        best_possible_score = 95476

    with open(filename) as file:
        map_data = maps.str_to_map(file.read())
        start = maps.get_position_of(map_data, START)
        end = maps.get_position_of(map_data, END)
        starting_direction = RIGHT
        result: set[vec2d.Vec2D] = set()

        context = Context(map_data, best_possible_score)

        search = [State(0, starting_direction, [start])]
        i = 0
        while search:
            i += 1
            state = search.pop(0)
            if state.position == end:
                maps.print_with_highlighted(map_data, state.path)
                result.update(state.path)
            else:
                search.extend(next_states(state, context))

    return len(result)
