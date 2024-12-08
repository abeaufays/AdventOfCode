import itertools

OPERATORS = ["+", "*", "||"]
OPERATIONS = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
    "||": lambda x, y: int(str(x) + str(y)),
}


def answer(input_: list[str]) -> int:
    result = 0
    for line in input_:
        test_value_raw, operands_raw = line.split(":")
        test_value = int(test_value_raw)

        operands = list(map(int, operands_raw.split()))
        for operators_setup in itertools.product(OPERATORS, repeat=len(operands) - 1):
            equation_result = OPERATIONS[operators_setup[0]](operands[0], operands[1])
            for operator, operand in zip(operators_setup[1:], operands[2:]):
                equation_result = OPERATIONS[operator](equation_result, operand)

            if equation_result == test_value:
                result += equation_result
                break
    return result


def tests():
    assert OPERATIONS["||"](12, 34) == 1234


tests()


with open("2024/7/test") as file:
    assert (result := answer(file.read().splitlines())) == (
        expected := 11387
    ), f"Test sample: {result} is not {expected}"

with open("2024/7/data") as file:
    print(answer(file.read().splitlines()))
