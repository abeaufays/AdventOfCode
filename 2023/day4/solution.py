from collections import defaultdict
import os
import re

dirname = os.path.dirname(os.path.realpath(__file__)) + "/"

regex = r"Card\s+(?P<number>\d+):(?P<winning_numbers>(\s+\d+)*)\s+\|(?P<numbers>((\s+\d+)*))"


def process(filename: str):
    times = defaultdict(lambda: 1)
    gain = 0
    with open(dirname + filename, "r") as file:
        for i, line in enumerate(file.readlines()):
            times[i]
            match = re.match(regex, line)
            card_id = int(match.group("number"))
            winning_numbers = list(map(int, match.group("winning_numbers").split()))
            numbers = list(map(int, match.group("numbers").split()))
            winning_numbers_in_numbers = set(winning_numbers) & set(numbers)

            for x in range(1, len(winning_numbers_in_numbers) + 1):
                times[i + x] += times[i]
            if winning_numbers_in_numbers:
                gain += 2 ** (len(winning_numbers_in_numbers) - 1)

    return gain, sum(times.values())


test_result = process("testdata.txt")
assert test_result == (13, 30), test_result


print(process("data.txt"))
