import pytest
import y24.d22.part1 as solution


def test_next_secret_number():
    secret_number = 123

    for expected in [
        15887950,
        16495136,
        527345,
        704524,
        1553684,
        12683156,
        11100544,
        12249484,
        7753432,
        5908254,
    ]:
        secret_number = solution.next_secret_number(secret_number)
        assert secret_number == expected


@pytest.mark.parametrize(
    ("start", "expected"),
    [
        (1, 8685429),
        (10, 4700978),
        (100, 15273692),
        (2024, 8667524),
    ],
)
def test_get_2000th_secret_number(start, expected):
    assert solution.get_2000th_secret_number(start) == expected


def test_answer():
    assert solution.answer("y24/d22/test") == 37327623
