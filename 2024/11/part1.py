def answer(stones: list[int]) -> int:
    for _ in range(25):
        stones = blink(stones)
    return len(stones)


def blink(stones: list[int]) -> list[int]:
    result = []
    for stone in stones:
        if stone == 0:
            result.append(1)
        elif not ((stone_size := len(as_str := str(stone))) % 2):
            result.append(int(as_str[: stone_size // 2]))
            result.append(int(as_str[stone_size // 2 :]))
        else:
            result.append(stone * 2024)
    return result


def test(result, expected):
    assert result == expected, f"{result} is not {expected}"


def test_suite_1():
    test(blink([0, 1, 10, 99, 999]), [1, 2024, 1, 0, 9, 9, 2021976])
    stones = [125, 17]
    for _ in range(6):
        stones = blink(stones)
    test(
        stones,
        [
            2097446912,
            14168,
            4048,
            2,
            0,
            2,
            4,
            40,
            48,
            2024,
            40,
            48,
            80,
            96,
            2,
            8,
            6,
            7,
            6,
            0,
            3,
            2,
        ],
    )

    test(answer([125, 17]), 55312)


test_suite_1()

print(answer([5, 62914, 65, 972, 0, 805922, 6521, 1639064]))
