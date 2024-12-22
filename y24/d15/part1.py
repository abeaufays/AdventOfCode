import numpy as np
import utils.maps as map_utils
from utils import vec2d

DIRECTIONS = {
    (UP := "^"): (-1, 0),
    (RIGHT := ">"): (0, 1),
    (DOWN := "v"): (1, 0),
    (LEFT := "<"): (0, -1),
}

EMPTY = "."
WALL = "#"
BOX = "O"
CHARACTER = "@"


class Map:
    def __init__(self, map_data: np.ndarray):
        self.data: np.ndarray = map_data
        self.character: vec2d.Vec2D = map_utils.get_position_of(self.data, CHARACTER)
        self.data[self.character] = EMPTY

    def move_character(self, direction: str) -> bool:
        """
        Returns True if character could move.
        """
        if direction not in DIRECTIONS.keys():
            raise ValueError

        position_in_front = vec2d.add(self.character, DIRECTIONS[direction])
        if self.data[position_in_front] == WALL:
            return False
        elif self.data[position_in_front] == EMPTY:
            self.character = position_in_front
            return True
        elif self.data[position_in_front] == BOX:
            following_position = position_in_front
            while self.data[following_position] == BOX:
                following_position = vec2d.add(
                    following_position, DIRECTIONS[direction]
                )
            if self.data[following_position] == EMPTY:
                self.data[position_in_front] = EMPTY
                self.data[following_position] = BOX
                self.character = position_in_front
                return True
            if self.data[following_position] == WALL:
                return False
        else:
            raise ValueError

    def compute_score(self) -> int:
        result = 0
        for idx, space in np.ndenumerate(self.data):
            if space == BOX:
                result += 100 * idx[0] + idx[1]

        return result


def get_data_from_file(filename: str):
    with open(filename) as file:
        map_data_raw, instructions = file.read().split("\n\n")
        map_data = map_utils.str_to_map(map_data_raw)
    return (map_data, instructions)


def answer(filename: str) -> int:
    map_data, instructions = get_data_from_file(filename)
    instructions = instructions.replace("\n", "")
    map = Map(map_data)
    for instruction in instructions:
        map.move_character(instruction)

    return map.compute_score()
