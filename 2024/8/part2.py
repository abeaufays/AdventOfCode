from collections import defaultdict
import operator
import numpy as np
from typing import TypeAlias
import itertools


EMPTY = "."

AntennaLocations: TypeAlias = dict[str, list[tuple[int, int]]]


def answer(map_data: np.ndarray) -> int:
    antenna_locations = map_antenna_locations(map_data)
    antinodes = find_antinodes(map_data, antenna_locations)
    _show_antinodes(map_data, antinodes)
    return len(antinodes)


def map_antenna_locations(input) -> AntennaLocations:
    antenna_mapping: AntennaLocations = defaultdict(list)
    for line_idx, line in enumerate(input):
        for col_idx, content in enumerate(line):
            if content != EMPTY:
                antenna_mapping[content].append((line_idx, col_idx))
    return antenna_mapping


def find_antinodes(
    map_data: np.ndarray, antenna_locations: AntennaLocations
) -> set[tuple[int, int]]:
    antinodes = set()
    for antennas in antenna_locations.values():
        for a, b in itertools.combinations(antennas, 2):
            difference = tuple(map(operator.sub, a, b))

            antinodes.add(a)
            antinodes.add(b)

            antinode_1 = tuple(map(operator.add, a, difference))
            while _is_in_map(antinode_1, map_data):
                antinodes.add(antinode_1)
                antinode_1 = tuple(map(operator.add, antinode_1, difference))

            antinode_2 = tuple(map(operator.sub, b, difference))
            while _is_in_map(antinode_2, map_data):
                antinodes.add(antinode_2)
                antinode_2 = tuple(map(operator.sub, antinode_2, difference))

    return antinodes


def _is_in_map(position: tuple[int, int], map: np.ndarray) -> bool:
    map_shape = map.shape
    return 0 <= position[0] <= map_shape[0] - 1 and 0 <= position[1] <= map_shape[1] - 1


def _show_antinodes(map_data: np.ndarray, antinodes: set[tuple[int, int]]):
    data = map_data.copy()
    for antinode in antinodes:
        data[antinode] = "#"
    print("\n".join("".join(line) for line in data))


with open("2024/8/test") as file:
    input = np.array([list(line.strip()) for line in file.readlines()])
    assert (result := answer(input)) == (
        expected := 34
    ), f"Test sample: {result} is not {expected}"

with open("2024/8/data") as file:
    input = np.array([list(line.strip()) for line in file.readlines()])
    print(answer(input))
