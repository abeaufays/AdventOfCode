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
LEFT_BOX = "["
RIGHT_BOX = "]"


def _scale_map(map_data: np.ndarray) -> np.ndarray:
    ### CHANGE SHOULD INCLUDE * instead of +
    ## map_data not same shape as result !!!!
    result = np.empty((map_data.shape[0], map_data.shape[1] * 2), str)
    for idx, content in np.ndenumerate(map_data):
        if content == EMPTY:
            result[(idx[0], idx[1] * 2)] = EMPTY
            result[(idx[0], idx[1] * 2 + 1)] = EMPTY
        if content == BOX:
            result[(idx[0], idx[1] * 2)] = LEFT_BOX
            result[(idx[0], idx[1] * 2 + 1)] = RIGHT_BOX
        if content == WALL:
            result[(idx[0], idx[1] * 2)] = WALL
            result[(idx[0], idx[1] * 2 + 1)] = WALL
        if content == CHARACTER:
            result[(idx[0], idx[1] * 2)] = CHARACTER
            result[(idx[0], idx[1] * 2 + 1)] = EMPTY
    return result


class Map:
    def __init__(self, map_data: np.ndarray):
        self.data: np.ndarray = _scale_map(map_data)
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
        elif self.data[position_in_front] in (LEFT_BOX, RIGHT_BOX):
            box_positions = [position_in_front]
            if direction in [UP, DOWN]:
                box_positions.append(
                    vec2d.add(position_in_front, DIRECTIONS[RIGHT])
                    if self.data[position_in_front] == LEFT_BOX
                    else vec2d.add(position_in_front, DIRECTIONS[LEFT])
                )
            idx = 0
            while idx < len(box_positions):
                current_box_position = box_positions[idx]
                front_of_current_box = vec2d.add(
                    current_box_position, DIRECTIONS[direction]
                )
                if self.data[front_of_current_box] == WALL:
                    return False
                if self.data[front_of_current_box] in (LEFT_BOX, RIGHT_BOX):
                    if front_of_current_box not in box_positions:
                        box_positions.append(front_of_current_box)
                    if direction in [UP, DOWN]:
                        other_side_of_front_box = (
                            vec2d.add(front_of_current_box, DIRECTIONS[RIGHT])
                            if self.data[front_of_current_box] == LEFT_BOX
                            else vec2d.add(front_of_current_box, DIRECTIONS[LEFT])
                        )

                        if other_side_of_front_box not in box_positions:
                            box_positions.append(other_side_of_front_box)
                idx += 1
            for position in box_positions[::-1]:
                next_position = vec2d.add(position, DIRECTIONS[direction])
                self.data[next_position] = self.data[position]
                self.data[position] = EMPTY
            self.character = vec2d.add(self.character, DIRECTIONS[direction])
            return True
        else:
            raise ValueError

    def compute_score(self) -> int:
        result = 0
        for idx, space in np.ndenumerate(self.data):
            if space == LEFT_BOX:
                result += 100 * idx[0] + idx[1]

        return result

    def show(self) -> None:
        self.data[self.character] = CHARACTER
        print(map_utils.to_str(self.data))
        self.data[self.character] = EMPTY


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
