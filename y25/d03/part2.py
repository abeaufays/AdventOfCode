def answer(filename: str) -> int:
    result = 0
    n = 12
    with open(filename) as file:
        for line in file:
            bank = list(map(int, line.strip()))
            joltage: list[int] = []
            start = 0
            for i in range(n):
                start = bank[start:].index(joltage[-1]) + 1 + start if joltage else 0
                end = -(n - i) + 1
                if end == 0:
                    end = None
                joltage.append(max(bank[start:end]))
            result += int("".join(map(str, joltage)))
    return result
