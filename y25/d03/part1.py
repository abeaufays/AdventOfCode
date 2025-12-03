def answer(filename: str) -> int:
    result = 0
    with open(filename) as file:
        for line in file:
            bank = list(map(int, line.strip()))
            first_digit = max(bank[:-1])
            second_digit = max(bank[bank.index(first_digit) + 1 :])
            result += int(first_digit * 10 + second_digit)
    return result
