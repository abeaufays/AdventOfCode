from typing import TextIO


def answer(file: TextIO) -> int:
    result = 0
    for line in file:
        report = [int(x) for x in line.split()]
        if is_report_safe(report):
            result += 1
    return result


def is_report_safe(report: list[int]) -> bool:
    is_increasing = report[0] < report[1]
    for first, second in zip(report[:-1], report[1:]):
        if (
            (is_increasing and first > second)
            or (not is_increasing and first < second)
            or (not (1 <= abs(first - second) <= 3))
        ):
            return False
    return True


if False:
    assert is_report_safe([1, 3, 6]), "Increasing OK"
    assert not is_report_safe([1, 3, 2]), "Not always increasing"
    assert not is_report_safe([1, 3, 8]), "Increasing too much"
    assert is_report_safe([8, 7, 6]), "Decreasing"
    assert not is_report_safe([8, 7, 7]), "Decreasing but not enough"
    assert not is_report_safe([8, 7, 9]), "Not always decreasing"
    assert not is_report_safe([8, 7, 2]), "Decreasing too much"

with open("2024/2/test") as file:
    assert (result := answer(file)) == (expected := 2), f"{result} is not {expected}"

with open("2024/2/data") as file:
    print(answer(file))
