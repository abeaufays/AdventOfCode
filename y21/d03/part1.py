def answer(filename: str) -> int:
    with open(filename) as file:
        lines = file.readlines()
        line_numbers = len(lines)
        data = [0] * (len(lines[0]) - 1)
        for line in lines:
            for index, digit in enumerate(map(int, line.strip())):
                data[index] += digit

    most_common_bits = "".join(["1" if x > line_numbers // 2 else "0" for x in data])
    gamma_rate = int(most_common_bits, 2)
    espilon_rate = int(
        "".join({"0": "1", "1": "0"}[bit] for bit in most_common_bits), 2
    )

    return gamma_rate * espilon_rate
