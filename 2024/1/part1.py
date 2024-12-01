from io import TextIOWrapper


def answer(inp: TextIOWrapper) -> int:
    left_list, right_list = _sanitize(inp)

    left_list.sort()
    right_list.sort()

    result = 0
    for left, right in zip(left_list, right_list):
        result += abs(left - right)

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
    assert (result := answer(file)) == (expected := 11), f"{result} is not {expected}"

with open("2024/1/data") as file:
    print(answer(file))
