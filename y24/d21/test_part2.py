import pytest
import y24.d21.part2 as solution


def test_answer():
    assert solution.answer("y24/d21/test") == 126384


def test_parse_file():
    assert solution.parse_file("y24/d21/test") == [
        "029A",
        "980A",
        "179A",
        "456A",
        "379A",
    ]


@pytest.mark.parametrize(
    ("code", "layout", "expected"),
    [
        ("029A", solution.CODE_LAYOUT_ID, "<A^A^^>AvvvA"),
        ("379A", solution.CODE_LAYOUT_ID, "^A^^<<A>>AvvvA"),
        (
            "<A^A^^>AvvvA",
            solution.INSTRUCTIONS_LAYOUT_ID,
            "v<<A^>>A<A>A<AAv>A^Av<AAA^>A",
        ),
    ],
)
def test_code_to_instructions(code, layout, expected):
    assert len(min(solution.code_to_instructions(code, layout), key=len)) == len(
        expected
    )


@pytest.mark.parametrize(
    ("code", "expected"),
    [
        (
            "029A",
            "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A",
        ),
        ("980A", "<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A"),
        (
            "179A",
            "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",
        ),
        ("456A", "<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A"),
        ("379A", "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"),
    ],
)
def test_enter_code(code, expected):
    assert len(solution.enter_code(code)) == len(expected)


def test_get_possible_instructions_doesnt_cross_x():
    assert "^>>A" not in solution.get_possible_instructions(
        "<", "A", solution.INSTRUCTIONS_LAYOUT_ID
    )
    assert "<vA" not in solution.get_possible_instructions(
        "^", "<", solution.INSTRUCTIONS_LAYOUT_ID
    )
    assert "v>>A" not in solution.get_possible_instructions(
        "1", "A", solution.CODE_LAYOUT_ID
    )
    assert "<<^^A" not in solution.get_possible_instructions(
        "A", "4", solution.CODE_LAYOUT_ID
    )

    assert "<A" in solution.get_possible_instructions("A", "0", solution.CODE_LAYOUT_ID)
    assert "vA" in solution.get_possible_instructions("2", "0", solution.CODE_LAYOUT_ID)
    assert "vvA" in solution.get_possible_instructions(
        "7", "1", solution.CODE_LAYOUT_ID
    )
    assert "^^A" in solution.get_possible_instructions(
        "1", "7", solution.CODE_LAYOUT_ID
    )
    assert ">>vA" in solution.get_possible_instructions(
        "1", "A", solution.CODE_LAYOUT_ID
    )
