import functools
import numpy as np
from utils import maps, vec2d


CODE_LAYOUT = maps.str_to_map(
    """
789
456
123
X0A""".lstrip()
)

INSTRUCTIONS_LAYOUT = maps.str_to_map(
    """
X^A
<v>""".lstrip()
)


def order_function(instruction: str) -> int:
    return vec2d.distance_manhattan(
        maps.get_position_of(INSTRUCTIONS_LAYOUT, instruction), (0, 2)
    )


def code_to_instructions(code: str, layout: np.ndarray) -> str:
    position = maps.get_position_of(layout, "A")
    result = ""
    for letter in code:
        letter_position = maps.get_position_of(layout, letter)
        up_number = position[0] - letter_position[0]
        left_number = position[1] - letter_position[1]
        buffer = ("<" if left_number > 0 else ">") * abs(left_number)
        buffer += ("^" if up_number > 0 else "v") * abs(up_number)
        result += "".join(sorted(buffer, key=order_function, reverse=False))
        result += "A"
        position = letter_position
    return result


def parse_file(filename: str) -> list[str]:
    with open(filename) as file:
        return file.read().splitlines()


def enter_code(code: str) -> str:
    result = code_to_instructions(code, CODE_LAYOUT)
    result = code_to_instructions(result, INSTRUCTIONS_LAYOUT)
    result = code_to_instructions(result, INSTRUCTIONS_LAYOUT)
    return result


def answer(filename: str) -> int:
    codes = parse_file(filename)
    return 0
