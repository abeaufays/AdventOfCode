from collections.abc import Generator

EMPTY = -1


# Change disk_map representation to list to handle file_id that are > 9
def answer(disk_map_input: str) -> int:
    disk_map = to_disk_map(disk_map_input)
    ordered_disk_map = order_disk_map(disk_map)
    return compute_checksum(ordered_disk_map)


def print_disk_map(disk_map: list[int]):
    print("".join(map(lambda x: "." if x == -1 else chr(65 + x), disk_map)))
    print("---")


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
    last_file_space_finder = get_last_filled_finder(current_map)

    # Improve index search to start from last index memory
    for last_file_space_idxs in last_file_space_finder:
        empty_space = find_first_empty_space_before(
            current_map,
            last_file_space_idxs[1] - last_file_space_idxs[0] + 1,
            last_file_space_idxs[1],
        )
        if not empty_space:
            continue
        if empty_space[0] > last_file_space_idxs[0]:
            break
        _swap(current_map, empty_space, last_file_space_idxs)

    return current_map


def find_first_empty_space_before(
    file_map: list[int], size: int, before: int
) -> tuple[int, int] | None:
    for idx, file in enumerate(file_map):
        if idx >= before:
            return None
        if file == EMPTY:
            chunk = file_map[idx : idx + size]
            if all(space == EMPTY for space in chunk) and len(chunk) == size:
                return (idx, idx + size - 1)
    return None


def get_last_filled_finder(
    file_map: list[int],
) -> Generator[tuple[int, int], None, None]:
    file_map_buffer = file_map.copy()
    current_id = None
    for idx, file_slot in enumerate(file_map_buffer[::-1]):
        if file_slot != EMPTY:
            if current_id is None:
                current_id, upper_bound = file_slot, len(file_map_buffer) - idx - 1
        if current_id is not None and current_id != file_slot:
            yield (len(file_map_buffer) - idx, upper_bound)
            if file_slot == EMPTY:
                upper_bound = None
                current_id = None
            else:
                current_id = file_slot
                upper_bound = len(file_map_buffer) - idx - 1


def _swap(input: list[int], idx1: tuple[int, int], idx2: tuple[int, int]) -> None:
    input[idx1[0] : idx1[1] + 1], input[idx2[0] : idx2[1] + 1] = (
        input[idx2[0] : idx2[1] + 1],
        input[idx1[0] : idx1[1] + 1],
    )


def compute_checksum(file_map: list[int]) -> int:
    result = 0
    for idx, file in enumerate(file_map):
        result += idx * file if file != EMPTY else 0
    return result


def test(result, expected):
    assert result == expected, f"{result} is not {expected}"


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
tested_finder = get_last_filled_finder(
    [1, 2, 2, EMPTY, 3, 3, 3, EMPTY, EMPTY, 4, 4, EMPTY]
)
test(
    next(tested_finder),
    (9, 10),
)
test(
    next(tested_finder),
    (4, 6),
)

test(
    find_first_empty_space_before(
        [
            0,
            0,
            EMPTY,
            1,
            1,
            1,
            EMPTY,
            EMPTY,
            EMPTY,
            2,
            3,
            EMPTY,
            EMPTY,
            4,
            4,
            EMPTY,
            EMPTY,
            EMPTY,
            EMPTY,
            5,
        ],
        3,
        20,
    ),
    (6, 8),
)

test_swap_data = [0, 1, 1, 1, 4, 0, 3, 3, 3]
_swap(test_swap_data, (1, 3), (6, 8))
test(test_swap_data, [0, 3, 3, 3, 4, 0, 1, 1, 1])

test(to_disk_map(test_value), test_value_as_disk_map)
# "00...111...2...333.44.5555.6666.777.888899"
test_value_as_disk_map_copy = test_value_as_disk_map.copy()
last_filled_finder = get_last_filled_finder(test_value_as_disk_map_copy)
test(next(last_filled_finder), (40, 41))
test(next(last_filled_finder), (36, 39))
test_value_as_disk_map_copy[32:34] = [-1, -1, -1]
test(next(last_filled_finder), (32, 34))

test(find_first_empty_space_before(test_value_as_disk_map, 2, 41), (2, 3))
test(
    order_disk_map(test_value_as_disk_map),
    [
        0,
        0,
        9,
        9,
        2,
        1,
        1,
        1,
        7,
        7,
        7,
        EMPTY,
        4,
        4,
        EMPTY,
        3,
        3,
        3,
        EMPTY,
        EMPTY,
        EMPTY,
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
        EMPTY,
        EMPTY,
        EMPTY,
        EMPTY,
        8,
        8,
        8,
        8,
        EMPTY,
        EMPTY,
    ],
)


test(answer(test_value), 2858)

failed_test = "8148586248547086332471526999672950794"
failed_disk_map = to_disk_map(failed_test)
print("######")
print_disk_map(failed_disk_map)
order_disk_map(failed_disk_map)
test(answer(failed_test), 62223)

with open("2024/9/data") as file:
    print(answer(file.read()))

# 15798666315464 too high
# I don't want to clean tests sorry
