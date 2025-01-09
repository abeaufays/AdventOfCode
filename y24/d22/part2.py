from collections import defaultdict

type Instruction = tuple[int, int, int, int]


def next_secret_number(secret: int) -> int:
    # shift 6 bits to the left, then copy previous last
    secret = (secret ^ (secret * 64)) % 16777216
    secret = (secret ^ (secret // 32)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216
    return secret


def answer(filename: str) -> int:
    with open(filename) as file:
        instructions_results: dict[Instruction, list] = defaultdict(list)
        for line in file.read().splitlines():
            secret = int(line)
            prices: list = [secret % 10]
            deltas: list = [None]
            instructions_seen_this_number: set[Instruction] = set()
            for idx in range(2_000):
                secret = next_secret_number(secret)
                deltas.append((secret % 10) - prices[idx])
                prices.append(secret % 10)

                if idx >= 3:
                    instruction = tuple(deltas[idx - 3 : idx + 1])
                    if instruction not in instructions_seen_this_number:
                        instructions_seen_this_number.add(instruction)
                        instructions_results[instruction].append(prices[idx])

    return max(sum(prices) for prices in instructions_results.values())
