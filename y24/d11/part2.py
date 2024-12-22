from collections import defaultdict
import functools


def answer(stones_input: list[int], repetitions: int) -> int:
    stones = {stone: 1 for stone in stones_input}
    for i in range(repetitions):
        # Got unlocked by this
        # print(f"Blink {i}, size {len(stones)}, set size {len(set(stones))}")
        stones = blink(stones)

    return sum(stones.values())


def blink(stones: dict[int, int]) -> dict[int, int]:
    result: dict[int, int] = defaultdict(int)
    for stone, number in stones.items():
        for new_stone in blink_stone(stone):
            result[new_stone] += number
    return result


@functools.cache
def blink_stone(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    elif not ((stone_size := len(as_str := str(stone))) % 2):
        return [int(as_str[: stone_size // 2]), int(as_str[stone_size // 2 :])]
    else:
        return [stone * 2024]


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

    test(answer([125, 17], 25), 55312)


print("Part 1 ", answer([5, 62914, 65, 972, 0, 805922, 6521, 1639064], 25))
print("Part 2 ", answer([5, 62914, 65, 972, 0, 805922, 6521, 1639064], 75))
