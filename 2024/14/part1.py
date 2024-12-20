from __future__ import annotations
from collections import defaultdict
import dataclasses
from functools import reduce
from typing import Self

NONE = -1
TOP_LEFT = 0
TOP_RIGHT = 1
BOTTOM_LEFT = 2
BOTTOM_RIGHT = 3


@dataclasses.dataclass
class Vec2D:
    x: int
    y: int

    def add_in_bounds(self: Self, other: Vec2D, bounds: tuple[int, int]) -> Vec2D:
        return Vec2D(x=(self.x + other.x) % bounds[0], y=(self.y + other.y) % bounds[1])


@dataclasses.dataclass
class Robot:
    position: Vec2D
    vector: Vec2D

    def get_position_quadrant(robot: Robot, width: int, height: int) -> int:
        is_leftside = robot.position.x < width // 2
        is_rightside = robot.position.x > width // 2
        is_topside = robot.position.y < height // 2
        is_botside = robot.position.y > height // 2
        if is_topside and is_leftside:
            return TOP_LEFT
        elif is_topside and is_rightside:
            return TOP_RIGHT
        elif is_botside and is_leftside:
            return BOTTOM_LEFT
        elif is_botside and is_rightside:
            return BOTTOM_RIGHT
        return NONE


def print_robot_map(robots: list[Robot], width: int, height: int):
    positions: dict[tuple[int, int], int] = defaultdict(int)
    for robot in robots:
        positions[(robot.position.x, robot.position.y)] += 1

    for line_idx in range(height):
        for col_idx in range(width):
            if (robot_count := positions[(col_idx, line_idx)]) != 0:
                print(robot_count, end="")
            else:
                print(" ", end="")
        print()


def get_map_context(filename: str) -> tuple[int, int]:
    if filename.endswith("test"):
        return (11, 7)
    elif filename.endswith("data"):
        return (101, 103)
    raise NotImplementedError


def get_data_from_file(filename: str) -> tuple[list[Robot], int, int]:
    with open(filename) as file:
        test_input_raw = file.read()
        robots = []
        for line in test_input_raw.split("\n"):
            position_raw, vector_raw = line.split()
            position_raw = position_raw.removeprefix("p=")
            vector_raw = vector_raw.removeprefix("v=")

            position = Vec2D(
                x=(position_tuple := tuple(map(int, position_raw.split(","))))[0],
                y=position_tuple[1],
            )
            vector = Vec2D(
                x=(position_tuple := tuple(map(int, vector_raw.split(","))))[0],
                y=position_tuple[1],
            )
            robots.append(Robot(position=position, vector=vector))
    return robots, *get_map_context(filename)


def process_second(robots: list[Robot], width: int, height: int) -> None:
    for robot in robots:
        robot.position = robot.position.add_in_bounds(
            robot.vector, bounds=(width, height)
        )


def compute_quadrants_scores(robots: list[Robot], width: int, height: int) -> list[int]:
    result = [0, 0, 0, 0]
    for robot in robots:
        quadrant = robot.get_position_quadrant(width, height)
        if quadrant != NONE:
            result[quadrant] += 1
    return result


def answer(filename: str) -> int:
    robots, width, height = get_data_from_file(filename)
    seconds = 100
    print_robot_map(robots, width, height)
    for _ in range(seconds):
        process_second(robots, width, height)
    print("–" * width)
    print_robot_map(robots, width, height)
    quadrants_scores = compute_quadrants_scores(robots, width, height)
    return reduce(lambda x, y: x * y, quadrants_scores)


def test(result, expected):
    assert result == expected, f"{result} is not {expected}"


test(answer("2024/14/test"), 1)
print(answer("2024/14/data"))
