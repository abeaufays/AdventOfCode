import utils.vec2d as vec2d


def test_distance_manhattan():
    assert vec2d.distance_manhattan((1, 1), (4, 4)) == 6
    assert vec2d.distance_manhattan((-1, 1), (4, 1)) == 5
    assert vec2d.distance_manhattan((-4, 4), (4, -4)) == 16
