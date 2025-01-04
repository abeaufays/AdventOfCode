import pytest
import y24.d19.part2 as solution


def test_answer():
    assert solution.answer("y24/d19/test") == 16


@pytest.mark.parametrize(
    ("pattern", "expected"),
    [
        ("brwrr", 2),
        ("bggr", 1),
        ("gbbr", 4),
        ("rrbgbr", 6),
        ("ubwu", 0),
        ("bwurrg", 1),
        ("brgr", 2),
        ("bbrgwb", 0),
    ],
)
def test_count_pattern_fulfilling_ways(pattern, expected):
    towels = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
    assert solution.count_pattern_fulfilling_ways(pattern, towels) == expected
