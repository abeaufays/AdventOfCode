from typing import TextIO


def answer(file: TextIO) -> int:
    result = 0
    for line in file:
        report = [int(x) for x in line.split()]
        if is_report_safe_with_removal(report):
            result += 1
    return result


def is_report_safe_with_removal(report: list[int]) -> bool:
    for i in range(len(report)):
        if is_report_safe(report[:i] + report[i + 1 :]):
            return True
    return False


def is_report_safe(report: list[int]) -> bool:
    diff_set = {i - j for i, j in zip(report[:-1], report[1:])}
    return diff_set.issubset({1, 2, 3}) or diff_set.issubset({-1, -2, -3})


if True:
    assert is_report_safe_with_removal(
        [4, 5, 4, 3, 2, 1]
    ), "Safe by removing the first one."

    assert is_report_safe_with_removal(
        [7, 6, 4, 2, 2]
    ), "Safe by removing the last one."
    assert is_report_safe_with_removal(
        [7, 6, 4, 2, 1]
    ), "Safe without removing any level."
    assert not is_report_safe_with_removal(
        [1, 2, 7, 8, 9]
    ), "Unsafe regardless of which level is removed."
    assert not is_report_safe_with_removal(
        [9, 7, 6, 2, 1]
    ), "Unsafe regardless of which level is removed."
    assert is_report_safe_with_removal(
        [1, 3, 2, 4, 5]
    ), "Safe by removing the second level, 3."
    assert is_report_safe_with_removal(
        [8, 6, 4, 4, 1]
    ), "Safe by removing the third level, 4."
    assert is_report_safe_with_removal(
        [1, 3, 6, 7, 9]
    ), "Safe without removing any level."


with open("2024/2/test") as file:
    assert (result := answer(file)) == (expected := 4), f"{result} is not {expected}"

with open("2024/2/data") as file:
    print(answer(file))
