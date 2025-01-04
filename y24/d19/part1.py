def is_pattern_possible(pattern: str, towels: list[str]) -> bool:
    search = [""]

    while search:
        current_state = search.pop()
        for towel in towels:
            new_state = current_state + towel

            if new_state == pattern:
                return True

            if pattern.startswith(new_state):
                search.append(new_state)

    return False


def answer(filename: str) -> int:
    with open(filename) as file:
        lines = file.read().splitlines()
        available_towels = lines[0].split(", ")
        patterns = lines[2:]

        return sum(
            is_pattern_possible(pattern, available_towels) for pattern in patterns
        )
