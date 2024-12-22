from io import TextIOWrapper
from collections import Counter


def answer(inp: TextIOWrapper) -> int:
    left_list, right_list = _sanitize(inp)

    right_list_counter = Counter(right_list)

    result = 0
    for i in left_list:
        result += i * right_list_counter[i]

    return result


def _sanitize(inp: TextIOWrapper) -> tuple[list[int], list[int]]:
    left_list: list[int] = []
    right_list: list[int] = []

    for line in inp:
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))

    return left_list, right_list


with open("2024/1/test") as file:
    assert (result := answer(file)) == (expected := 31), f"{result} is not {expected}"

with open("2024/1/data") as file:
    print(answer(file))
