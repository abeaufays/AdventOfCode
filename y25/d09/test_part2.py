import y25.d09.part2 as solution


def test_answer():
    assert solution.answer("y25/d09/test") == 24


def test_is_in_between():
    assert solution.is_in_between((1, 1), (3, 3), (2, 2)) is True
    assert solution.is_in_between((1, 1), (3, 3), (1, 1)) is False
    assert solution.is_in_between((1, 1), (3, 3), (3, 3)) is False
    assert solution.is_in_between((1, 1), (3, 3), (2, 1)) is False
    assert solution.is_in_between((1, 1), (3, 3), (1, 2)) is False
    assert solution.is_in_between((1, 1), (3, 3), (0, 0)) is False
    assert solution.is_in_between((1, 1), (3, 3), (4, 4)) is False
    assert solution.is_in_between((3, 3), (1, 1), (2, 2)) is True
    assert solution.is_in_between((0, 0), (5, 5), (3, 3)) is True
    assert solution.is_in_between((0, 5), (5, 0), (2, 2)) is True
