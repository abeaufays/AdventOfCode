from part1 import Robot, Vec2D, BOTTOM_LEFT, BOTTOM_RIGHT, TOP_LEFT, TOP_RIGHT, NONE


class TestVec2:
    def test_add_in_bounds(self):
        first = Vec2D(1, 1)

        assert first.add_in_bounds(Vec2D(1, 1), (10, 10)) == Vec2D(2, 2)
        assert first.add_in_bounds(Vec2D(3, 3), (3, 3)) == Vec2D(1, 1)
        assert first.add_in_bounds(Vec2D(-3, -3), (10, 10)) == Vec2D(8, 8)


class TestRobot:
    def test_get_position_quadrant(self):
        robot = Robot(Vec2D(2, 2), Vec2D(0, 0))

        assert robot.get_position_quadrant(5, 5) == NONE
        assert robot.get_position_quadrant(9, 5) == NONE
        assert robot.get_position_quadrant(5, 9) == NONE
        assert robot.get_position_quadrant(3, 3) == BOTTOM_RIGHT
        assert robot.get_position_quadrant(11, 11) == TOP_LEFT
        assert robot.get_position_quadrant(3, 11) == TOP_RIGHT
        assert robot.get_position_quadrant(11, 3) == BOTTOM_LEFT
