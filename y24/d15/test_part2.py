import numpy as np
from utils import maps
from y24.d15 import part2


class TestMap:
    def test_answer(
        self,
    ):
        assert part2.answer("y24/d15/test") == 9021

    def test_map_creation(self):
        expected_map = """
####################
##....[]....[]..[]##
##............[]..##
##..[][]....[]..[]##
##....[]......[]..##
##[]##....[]......##
##[]....[]....[]..##
##..[][]..[]..[][]##
##........[]......##
####################""".lstrip()

        map_data, _ = part2.get_data_from_file("y24/d15/test")
        map = part2.Map(map_data)
        assert np.array_equal(map.data, maps.str_to_map(expected_map))
        assert map.character == (4, 8)

    def test_move_character(self):
        initial_map = """
#######
#.....#
#..O..#
#.@O..#
#.....#
#######""".lstrip()
        expected_initial_map = """
##############
##..........##
##....[]....##
##....[]....##
##..........##
##############""".lstrip()
        map = part2.Map(maps.str_to_map(initial_map))
        assert np.array_equal(map.data, maps.str_to_map(expected_initial_map))

        instructions = ">><^^>v"
        expected_final_map = """
##############
##..........##
##..........##
##....[]....##
##.....[]...##
##############""".lstrip()
        for instruction in instructions:
            map.move_character(instruction)

        assert np.array_equal(map.data, maps.str_to_map(expected_final_map))

    def test_move_two_boxes_up(self):
        initial_map = """
#####
#...#
#.O.#
#.O.#
#.@.#
#####""".lstrip()
        expected_initial_map = """
##########
##......##
##..[]..##
##..[]..##
##......##
##########""".lstrip()

        map = part2.Map(maps.str_to_map(initial_map))
        assert np.array_equal(map.data, maps.str_to_map(expected_initial_map))

        expected_final_map = """
##########
##..[]..##
##..[]..##
##......##
##......##
##########""".lstrip()
        map.move_character(part2.UP)
        assert np.array_equal(map.data, maps.str_to_map(expected_final_map))
