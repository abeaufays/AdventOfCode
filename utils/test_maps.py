from utils import maps


def test_get_positon_of():
    map_data = maps.str_to_map("""A...
.X..
....
...Y
""")
    assert maps.get_position_of(map_data, "X") == (1, 1)
    assert maps.get_position_of(map_data, "A") == (0, 0)
    assert maps.get_position_of(map_data, "Y") == (3, 3)


def test_is_position_in_map():
    map_data = maps.str_to_map(
        """
...
.X.
...""".lstrip()
    )

    assert maps.is_position_in_map((0, 0), map_data)
    assert maps.is_position_in_map((2, 2), map_data)
    assert maps.is_position_in_map((1, 1), map_data)
    assert not maps.is_position_in_map((-1, 0), map_data)
    assert not maps.is_position_in_map((0, -1), map_data)
    assert not maps.is_position_in_map((3, 0), map_data)
    assert not maps.is_position_in_map((0, 3), map_data)
