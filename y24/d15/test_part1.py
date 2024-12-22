from y24.d15 import part1
from utils import maps


def test_answer():
    assert part1.answer("y24/d15/small_test") == 2028
    assert part1.answer("y24/d15/test") == 10092


class TestMap:
    def test_move_character(self):
        map_str = """######
#.#..#
#O@..#
#.O..#
#.O..#
#.O..#
#....#
######
"""
        map = part1.Map(maps.str_to_map(map_str))
        assert not map.move_character(part1.LEFT)
        assert not map.move_character(part1.UP)
        assert map.character == (2, 2)

        map = part1.Map(maps.str_to_map(map_str))
        assert map.move_character(part1.RIGHT)
        assert map.character == (2, 3)
        assert map.data[(2, 3)] == part1.EMPTY

        map = part1.Map(maps.str_to_map(map_str))
        assert map.move_character(part1.DOWN)
        assert map.character == (3, 2)
        assert map.data[(3, 2)] == part1.EMPTY
        assert map.data[(6, 2)] == part1.BOX
