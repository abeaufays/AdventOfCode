def parse_file(filename):
    with open(filename) as file:
        fresh_ranges_raw, available_items_raw = file.read().split("\n\n")

    fresh_ranges = list(
        map(lambda s: tuple(map(int, s.split("-"))), fresh_ranges_raw.split("\n"))
    )
    # available_items = list(map(int, available_items_raw.split("\n")))
    return fresh_ranges


def resolve_ranges(fresh_ranges: list[tuple[int, int]]) -> set[tuple[int, int]]:
    resolved_ranges: set[tuple[int, int]] = set()

    for fresh_range in fresh_ranges:
        min_to_replace, max_to_replace = None, None
        to_remove = set()

        for resolved_range in resolved_ranges:
            if (
                fresh_range[0] <= resolved_range[0]
                and resolved_range[1] <= fresh_range[1]
            ):
                # We remove already resolved ranges encompassed in new one
                to_remove.add(resolved_range)
                continue

            if resolved_range[0] <= fresh_range[0] <= resolved_range[1]:
                min_to_replace = resolved_range
            if resolved_range[0] <= fresh_range[1] <= resolved_range[1]:
                max_to_replace = resolved_range

            if min_to_replace and max_to_replace:
                break

        new_range = fresh_range
        if to_remove:
            resolved_ranges -= to_remove

        if min_to_replace:
            resolved_ranges.remove(min_to_replace)
            new_range = (min_to_replace[0], new_range[1])
        if max_to_replace:
            if max_to_replace in resolved_ranges:
                resolved_ranges.remove(max_to_replace)
            new_range = (new_range[0], max_to_replace[1])

        resolved_ranges.add(new_range)
    return resolved_ranges


def answer(filename: str) -> int:
    fresh_ranges = parse_file(filename)

    resolved_ranges = resolve_ranges(fresh_ranges)

    result = 0
    for resolved_range in resolved_ranges:
        result += resolved_range[1] - resolved_range[0] + 1

    return result
