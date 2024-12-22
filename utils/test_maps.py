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
