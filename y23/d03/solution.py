from collections import defaultdict
from utils import interval_intersection
import re
import os

dirname = os.path.dirname(os.path.realpath(__file__)) + "/"


def get_linked_part_numbers(i: int, j: int, numbers: dict[int, list]):
    for t in [x + i for x in [-1, 0, 1] if 0 <= x + i <= len(numbers)]:
        for number in numbers[t]:
            if interval_intersection(number["span"], [j - 1, j + 1]):
                yield number


def process(filename: str):
    data: list[str] = []
    numbers = defaultdict(list)
    gear_ratio = 0
    with open(dirname + filename, "r") as file:
        data = file.readlines()

        for i, line in enumerate(data):
            number_matches: list[re.Match] = re.finditer(r"\d+", line)
            for match in number_matches:
                span = list(match.span())
                span[1] -= 1
                numbers[i].append({"number": match.group(0), "span": span, "line": i})

        part_numbers = []
        for i, line in enumerate(data):
            for j, letter in enumerate(line):
                if letter != "." and not letter.isdigit() and letter != "\n":
                    for part_number in get_linked_part_numbers(i, j, numbers):
                        if part_number not in part_numbers:
                            part_numbers.append(part_number)
                if (
                    letter == "*"
                    and len(
                        linked_part_numbers := list(
                            get_linked_part_numbers(i, j, numbers)
                        )
                    )
                    == 2
                ):
                    gear_ratio += int(linked_part_numbers[0]["number"]) * int(
                        linked_part_numbers[1]["number"]
                    )

    return sum(int(value["number"]) for value in part_numbers), gear_ratio


test_result = process("testdata0.txt")
assert test_result == (4361, 467835), test_result

# test_result = process("testdata1.txt")
# assert test_result == 925, test_result

# test_result = process("testdata2.txt")
# assert test_result == 40, test_result

print(process("data.txt"))
