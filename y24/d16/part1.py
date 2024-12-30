from typing import Protocol
import numpy as np
from dataclasses import dataclass
from utils import maps, vec2d
from sortedcontainers import SortedKeyList

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
class Node:
    score: int
    position: vec2d.Vec2D
    direction: vec2d.Vec2D


@dataclass
class Context:
    map_data: np.ndarray
    visited_positions: set[vec2d.Vec2D]


class Action(Protocol):
    def can_proceed(self, context: Context, node: Node) -> bool: ...

    def proceed(self, context: Context, node: Node) -> Node: ...


class Advance(Action):
    def can_proceed(self, context: Context, node: Node) -> bool:
        front_position = vec2d.add(node.position, node.direction)
        return (
            context.map_data[front_position] in (EMPTY, END)
            and front_position not in context.visited_positions
        )

    def proceed(self, context: Context, node: Node) -> Node:
        front_position = vec2d.add(node.position, node.direction)
        context.visited_positions.add(front_position)
        return Node(
            score=node.score + 1, position=front_position, direction=node.direction
        )


class Turn(Action):
    def __init__(self, clockwise: bool):
        self.clockwise = clockwise

    def can_proceed(self, context: Context, node: Node) -> bool:
        current_direction_idx = DIRECTIONS.index(node.direction)
        next_direction_idx = (
            current_direction_idx + 1 if self.clockwise else current_direction_idx - 1
        )
        next_direction = DIRECTIONS[next_direction_idx % 4]
        following_front_position = vec2d.add(node.position, next_direction)
        return (
            context.map_data[following_front_position] in (EMPTY, END)
            and following_front_position not in context.visited_positions
        )

    def proceed(self, context: Context, node: Node) -> Node:
        current_direction_idx = DIRECTIONS.index(node.direction)
        next_direction_idx = (
            current_direction_idx + 1 if self.clockwise else current_direction_idx - 1
        )
        next_direction = DIRECTIONS[next_direction_idx % 4]
        return Node(
            score=node.score + 1_000, position=node.position, direction=next_direction
        )


ACTIONS: list[Action] = [Advance(), Turn(True), Turn(False)]


def answer(filename: str) -> int:
    with open(filename) as file:
        map_data = maps.str_to_map(file.read())
        start = maps.get_position_of(map_data, START)
        end = maps.get_position_of(map_data, END)
        starting_direction = RIGHT

        search = SortedKeyList(
            [Node(0, start, starting_direction)], key=lambda x: x.score
        )
        context = Context(map_data=map_data, visited_positions=set())

        while True:
            # Ensure we don't get back on places we already visited
            current = search.pop(0)
            for action in ACTIONS:
                if action.can_proceed(context, current):
                    next = action.proceed(context, current)
                    if next.position == end:
                        return next.score
                    search.add(next)

    raise ValueError
