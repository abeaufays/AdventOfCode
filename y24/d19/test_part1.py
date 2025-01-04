import pytest
import y24.d19.part1 as solution


def test_answer():
    assert solution.answer("y24/d19/test") == 6


@pytest.mark.parametrize(
    ("pattern", "expected"),
    [
        ("brwrr", True),
        ("bggr", True),
        ("gbbr", True),
        ("rrbgbr", True),
        ("ubwu", False),
        ("bwurrg", True),
        ("brgr", True),
        ("bbrgwb", False),
    ],
)
def test_is_pattern_possible(pattern, expected):
    towels = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
    assert solution.is_pattern_possible(pattern, towels) == expected
