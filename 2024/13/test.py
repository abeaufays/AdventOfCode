import solution


def test_parse_setup():
    input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400"""
    assert solution.parse_setup(input) == (94, 34, 22, 67, 8400, 5400)
    input = """Button A: X-4, Y-4
Button B: X+22, Y+67
Prize: X=-400, Y=5400"""
    assert solution.parse_setup(input) == (-4, -4, 22, 67, -400, 5400)


def test_full_part1():
    with open("2024/13/test") as file:
        assert solution.part1(file.read()) == 480
