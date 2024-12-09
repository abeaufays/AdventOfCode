from collections.abc import Generator


EMPTY = -1


# Change disk_map representation to list to handle file_id that are > 9
def answer(disk_map_input: str) -> int:
    disk_map = to_disk_map(disk_map_input)
    ordered_disk_map = order_disk_map(disk_map)
    return compute_checksum(ordered_disk_map)


def to_disk_map(disk_map_input: str) -> list[int]:
    result: list[int] = []
    file_id = 0
    for idx, disk_space_repr in enumerate(disk_map_input):
        if idx % 2 == 0:
            result.extend(file_id for _ in range(int(disk_space_repr)))
            file_id += 1
        else:
            result.extend(EMPTY for _ in range(int(disk_space_repr)))
    return result


def order_disk_map(disk_map: list[int]) -> list[int]:
    current_map = disk_map.copy()
    first_empty_space_finder = get_first_empty_finder(current_map)
    last_file_space_finder = get_last_filled_finder(current_map)

    # Improve index search to start from last index memory
    while (first_empty_space_idx := next(first_empty_space_finder)) < (
        last_file_space_idx := next(last_file_space_finder)
    ):
        _swap(current_map, first_empty_space_idx, last_file_space_idx)

    return current_map


def get_first_empty_finder(file_map: list[int]) -> Generator[int, None, None]:
    for idx, file in enumerate(file_map):
        if file == EMPTY:
            yield idx


def get_last_filled_finder(file_map: list[int]) -> Generator[int, None, None]:
    for idx, file in enumerate(file_map[::-1]):
        if file != EMPTY:
            yield len(file_map) - idx - 1


def _swap(input: list[int], idx1: int, idx2: int) -> None:
    input[idx1], input[idx2] = input[idx2], input[idx1]


def compute_checksum(file_map: list[int]) -> int:
    result = 0
    for idx, file in enumerate(file_map):
        result += idx * file if file != EMPTY else 0
    return result


test_value = "2333133121414131402"
test_value_as_disk_map = [
    0,
    0,
    EMPTY,
    EMPTY,
    EMPTY,
    1,
    1,
    1,
    EMPTY,
    EMPTY,
    EMPTY,
    2,
    EMPTY,
    EMPTY,
    EMPTY,
    3,
    3,
    3,
    EMPTY,
    4,
    4,
    EMPTY,
    5,
    5,
    5,
    5,
    EMPTY,
    6,
    6,
    6,
    6,
    EMPTY,
    7,
    7,
    7,
    EMPTY,
    8,
    8,
    8,
    8,
    9,
    9,
]
assert (
    next(
        get_last_filled_finder([1, 2, 2, EMPTY, 3, 3, 3, EMPTY, EMPTY, 4, EMPTY, EMPTY])
    )
    == 9
)
assert to_disk_map(test_value) == test_value_as_disk_map
# "00...111...2...333.44.5555.6666.777.888899"
assert order_disk_map(test_value_as_disk_map) == [
    0,
    0,
    9,
    9,
    8,
    1,
    1,
    1,
    8,
    8,
    8,
    2,
    7,
    7,
    7,
    3,
    3,
    3,
    6,
    4,
    4,
    6,
    5,
    5,
    5,
    5,
    6,
    6,
    EMPTY,
    EMPTY,
    EMPTY,
    EMPTY,
    EMPTY,
    EMPTY,
    EMPTY,
    EMPTY,
    EMPTY,
    EMPTY,
    EMPTY,
    EMPTY,
    EMPTY,
    EMPTY,
]

assert (result := answer(test_value)) == (
    expected := 1928
), f"Test sample: {result} is not {expected}"

with open("2024/9/data") as file:
    print(answer(file.read()))

# 90950452031 first try, wrong because a file_id = 10 will be understood as two files 1 and 0
