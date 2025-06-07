import y24.d24.part1 as solution


def test_answer():
    assert solution.answer("y24/d24/test") == 2024


def test_parse():
    with open("y24/d24/test") as file:
        data = solution.parse_file(file)

    # Initial
    assert solution.access("x00")
    assert not solution.access("x01")
    assert solution.access("x02")
    assert solution.access("x03")
    assert not solution.access("x04")
    assert solution.access("y00")
    assert solution.access("y01")
    assert solution.access("y02")
    assert solution.access("y03")
    assert solution.access("y04")

    # Simple
    assert solution.access("fst")  # x00 OR x03 -> fst / 1 or 1
    assert not solution.access("kjc")  # x04 AND y00 -> kjc / 0 and 1
    assert solution.access("fgs")  # y04 OR y02 -> fgs / 1 or 1
    assert solution.access("psh")  # y03 OR y00 -> psh / 1 or 1

    # Combination
    assert not solution.access("tgd")  # psh XOR fgs -> tgd / 1 xor 1
