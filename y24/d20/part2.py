import numpy as np
from utils import maps, vec2d

WALL = "#"
TRACK = "."
START = "S"
END = "E"

CHEAT_DISTANCE = 20

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
        if vec2d.distance_manhattan(tile_from, adjacent_tile) <= CHEAT_DISTANCE
    ]


def parse_file(filename: str) -> tuple[np.ndarray, int]:
    with open(filename) as file:
        lines = file.readlines()
        picoseconds_to_save = int(lines[0])

        map_data = maps.str_to_map("".join(lines[1:]))
        return map_data, picoseconds_to_save


def answer(filename: str) -> int:
    map_data, picoseconds_to_save = parse_file(filename)

    path = find_path(map_data)
    result = 0
    debug = []
    for idx, tile in enumerate(path):
        jumpable_tiles = get_jumpable_tiles(path[idx + 1 :], tile)
        for jumpable_tile in jumpable_tiles:
            if path.index(
                jumpable_tile
            ) - idx >= picoseconds_to_save + vec2d.distance_manhattan(
                tile, jumpable_tile
            ):
                result += 1

                debug.append((tile, jumpable_tile, path.index(jumpable_tile) - idx))
    return result
