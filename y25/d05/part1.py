def parse_file(filename):
    with open(filename) as file:
        fresh_ranges_raw, available_items_raw = file.read().split("\n\n")

    fresh_ranges = list(
        map(lambda s: tuple(map(int, s.split("-"))), fresh_ranges_raw.split("\n"))
    )
    available_items = list(map(int, available_items_raw.split("\n")))
    return fresh_ranges, available_items


def answer(filename: str) -> int:
    fresh_ranges, available_items = parse_file(filename)
    result = 0
    for available_item in available_items:
        if any(
            fresh_range[0] <= available_item <= fresh_range[1]
            for fresh_range in fresh_ranges
        ):
            result += 1

    return result
