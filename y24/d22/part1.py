def mix(secret: int, value: int) -> int:
    return secret ^ value


def prune(secret: int) -> int:
    return secret % 16777216


def next_secret_number(secret: int) -> int:
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, int(secret / 32)))
    secret = prune(mix(secret, secret * 2048))
    return secret


def get_2000th_secret_number(secret: int) -> int:
    for _ in range(2_000):
        secret = next_secret_number(secret)
    return secret


def answer(filename: str) -> int:
    with open(filename) as file:
        return sum(
            map(lambda x: get_2000th_secret_number(int(x)), (file.read().splitlines()))
        )
