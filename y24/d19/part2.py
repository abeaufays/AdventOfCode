def count_pattern_fulfilling_ways(pattern: str, towels: list[str]) -> int:
    ways_to_go_at_index = [0 for _ in range(len(pattern) + 1)]
    ways_to_go_at_index[0] = 1

    for idx, ways_nb in enumerate(ways_to_go_at_index):
        if ways_nb == 0:
            continue
        for towel in towels:
            if idx + len(towel) > len(pattern):
                continue
            if pattern[idx:].startswith(towel):
                ways_to_go_at_index[idx + len(towel)] += ways_nb

    return ways_to_go_at_index[-1]


def answer(filename: str) -> int:
    with open(filename) as file:
        lines = file.read().splitlines()
        available_towels = lines[0].split(", ")
        patterns = lines[2:]

        return sum(
            count_pattern_fulfilling_ways(pattern, available_towels)
            for pattern in patterns
        )
