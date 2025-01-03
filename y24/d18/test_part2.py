import numpy as np
import pytest
from utils import maps
import y24.d18.part2 as solution


def test_answer():
    assert solution.answer("y24/d18/test") == (6, 1)


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """
.....
.###.
.#...
.#.##
.##..""".lstrip(),
            False,
        ),
        (
            """
.....
.###.
.#...
.#.##
.#...""".lstrip(),
            True,
        ),
    ],
)
def test_is_end_reachable(input, expected):
    map_data = maps.str_to_map(input)

    corrupted_positions = [
        (x[0], x[1]) for x in np.transpose(np.where(map_data == solution.CORRUPTED))
    ]
    context = solution.Context(map_data.shape, corrupted_positions)

    assert solution.is_end_reachable(context) == expected
