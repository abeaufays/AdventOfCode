import numpy as np
from utils import maps, vec2d

WALL = "#"
TRACK = "."
START = "S"
END = "E"


DIRECTIONS = [
    UP := (-1, 0),
    RIGHT := (0, 1),
    DOWN := (1, 0),
    LEFT := (0, -1),
]


def find_path(map_data: np.ndarray) -> list[vec2d.Vec2D]:
    start = maps.get_position_of(map_data, START)
    path = [start]
    ended = False
    while not ended:
        for direction in DIRECTIONS:
            next_position = vec2d.add(path[-1], direction)
            if len(path) >= 2 and next_position == path[-2]:
                continue
            if map_data[next_position] == TRACK:
                path.append(next_position)
                break
            if map_data[next_position] == END:
                path.append(next_position)
                ended = True
                break

    return path


def get_jumpable_tiles(
    path: list[vec2d.Vec2D], tile_from: vec2d.Vec2D
) -> list[vec2d.Vec2D]:
    return [
        adjacent_tile
        for adjacent_tile in path
        if vec2d.distance_manhattan(tile_from, adjacent_tile) <= 2
    ]


def answer(filename: str) -> int:
    with open(filename) as file:
        lines = file.readlines()
        picoseconds_to_save = int(lines[0])

        map_data = maps.str_to_map("".join(lines[1:]))

        path = find_path(map_data)
        result = 0
        for idx, tile in enumerate(path):
            jumpable_tiles = get_jumpable_tiles(path[idx + 1 :], tile)
            for jumpable_tile in jumpable_tiles:
                if path.index(jumpable_tile) - idx >= picoseconds_to_save + 2:
                    result += 1
    return result
