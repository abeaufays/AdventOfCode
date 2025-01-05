from utils import maps
import y24.d20.part1 as solution


def test_answer():
    # we test for 50 picoseconds saved at least
    assert solution.answer("y24/d20/test") == 1


def test_find_path():
    raw_map_data = """
#####
#S..#
###.#
#...#
#.###
#..E#
#####""".lstrip()
    map_data = maps.str_to_map(raw_map_data)

    expected = [
        (1, 1),
        (1, 2),
        (1, 3),
        (2, 3),
        (3, 3),
        (3, 2),
        (3, 1),
        (4, 1),
        (5, 1),
        (5, 2),
        (5, 3),
    ]

    assert solution.find_path(map_data) == expected


def test_get_jumpable_tiles():
    raw_map_data = """
#####
#S..#
###.#
#...#
#.###
#..E#
#####""".lstrip()
    map_data = maps.str_to_map(raw_map_data)

    path = solution.find_path(map_data)

    tile = (3, 3)
    assert solution.get_jumpable_tiles(path[path.index(tile) + 1 :], tile) == [
        (3, 2),
        (3, 1),
        (5, 3),
    ]
