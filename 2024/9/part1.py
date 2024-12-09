EMPTY = "."


# Change disk_map representation to list to handle file_id that are > 9
def answer(disk_map_input: str) -> int:
    disk_map = to_disk_map(disk_map_input)
    ordered_disk_map = order_disk_map(disk_map)
    return compute_checksum(ordered_disk_map)


def to_disk_map(disk_map: str) -> str:
    result = ""
    file_id = 0
    for idx, disk_space_repr in enumerate(disk_map):
        if idx % 2 == 0:
            result += str(file_id) * int(disk_space_repr)
            file_id += 1
        else:
            result += EMPTY * int(disk_space_repr)
    return result


def order_disk_map(disk_map: str) -> str:
    current_map = list(disk_map)
    first_empty_space_idx = current_map.index(EMPTY)
    last_file_space_idx = last_filled_index(current_map)

    # Improve index search to start from last index memory
    while first_empty_space_idx < last_file_space_idx:
        _swap(current_map, first_empty_space_idx, last_file_space_idx)
        first_empty_space_idx = current_map.index(EMPTY)
        last_file_space_idx = last_filled_index(current_map)
    return "".join(current_map)


def last_filled_index(file_map: list) -> int:
    for idx, file in enumerate(file_map[::-1]):
        if file != EMPTY:
            return len(file_map) - idx - 1
    return 0


def _swap(input: list, idx1: int, idx2: int) -> None:
    input[idx1], input[idx2] = input[idx2], input[idx1]


def compute_checksum(file_map: str) -> int:
    result = 0
    for idx, file in enumerate(file_map):
        result += idx * int(file) if file != EMPTY else 0
    return result


test_value = "2333133121414131402"
assert last_filled_index(list("qwer.t..")) == 5
assert to_disk_map(test_value) == "00...111...2...333.44.5555.6666.777.888899"
assert (
    order_disk_map("00...111...2...333.44.5555.6666.777.888899")
    == "0099811188827773336446555566.............."
)
assert (result := answer(test_value)) == (
    expected := 1928
), f"Test sample: {result} is not {expected}"

with open("2024/9/data") as file:
    print(answer(file.read()))

# 90950452031 first try, wrong because a file_id = 10 will be understood as two files 1 and 0
