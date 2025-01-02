import y24.d17.part1 as part1


def test_parse_input():
    input = """
Register A: 123
Register B: 456
Register C: 678

Program: 0,1,5,4,3,0""".lstrip()
    assert part1.parse(input) == part1.Device([123, 456, 678], [0, 1, 5, 4, 3, 0])


def test_answer():
    assert part1.answer("y24/d17/test") == "4,6,3,5,6,3,5,2,1,0"
