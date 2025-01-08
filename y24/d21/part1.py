import functools
from itertools import product
from utils import maps


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

CODE_LAYOUT_ID = "CODE"
INSTRUCTIONS_LAYOUT_ID = "INSTRUCTION"

LAYOUTS = {CODE_LAYOUT_ID: CODE_LAYOUT, INSTRUCTIONS_LAYOUT_ID: INSTRUCTIONS_LAYOUT}


@functools.cache
def get_possible_instructions(from_: str, to_: str, layout_id: str) -> set[str]:
    layout = LAYOUTS[layout_id]
    from_position = maps.get_position_of(layout, from_)
    to_position = maps.get_position_of(layout, to_)
    x_position = maps.get_position_of(layout, "X")

    up_number = from_position[0] - to_position[0]
    left_number = from_position[1] - to_position[1]

    horizontal_part = ("<" if left_number > 0 else ">") * abs(left_number)
    vertical_part = ("^" if up_number > 0 else "v") * abs(up_number)
    result = set()

    if not (
        (same_column := from_position[1] == x_position[1])
        and (
            will_cross := to_position[0] >= x_position[0]
            if up_number >= 0
            else to_position[0] <= x_position[0]
        )
    ):
        result |= {vertical_part + horizontal_part + "A"}

    if not (
        (same_line := from_position[0] == x_position[0])
        and (
            will_cross := to_position[1] <= x_position[1]
            if left_number >= 0
            else to_position[1] >= x_position[1]
        )
    ):
        result |= {horizontal_part + vertical_part + "A"}

    return result


@functools.cache
def code_to_instructions(code: str, layout_id: str) -> set[str]:
    start = "A"
    results = {""}
    for target in code:
        new_instructions = get_possible_instructions(start, target, layout_id)
        results = set(
            "".join(instructions) for instructions in product(results, new_instructions)
        )
        start = target

    return results


def parse_file(filename: str) -> list[str]:
    with open(filename) as file:
        return file.read().splitlines()


def enter_code(code: str) -> str:
    final_instruction = set()
    first_instructions = code_to_instructions(code, CODE_LAYOUT_ID)
    for first_instruction in first_instructions:
        second_instructions = code_to_instructions(
            first_instruction, INSTRUCTIONS_LAYOUT_ID
        )
        for second_instruction in second_instructions:
            third_instuctions = code_to_instructions(
                second_instruction, INSTRUCTIONS_LAYOUT_ID
            )
            final_instruction.update(third_instuctions)
    return min(final_instruction, key=len)


def answer(filename: str) -> int:
    codes = parse_file(filename)
    result = 0
    for code in codes:
        numeric_part = int(code[:-1])
        shortest_sequence_size = len(enter_code(code))
        result += numeric_part * shortest_sequence_size
    return result
