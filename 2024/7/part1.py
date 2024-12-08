import itertools
import functools

OPERATORS = ["+", "*"]


def answer(input_: list[str]) -> int:
    result = 0
    for line in input_:
        test_value_raw, operands_raw = line.split(":")
        test_value = int(test_value_raw)

        operands = operands_raw.split()
        for operators in itertools.product(OPERATORS, repeat=len(operands) - 1):
            equation = [
                operands[0],
                *(
                    x + y
                    for x, y in zip(
                        operators,
                        operands[1:],
                    )
                ),
            ]
            equation_result = int(
                functools.reduce(lambda x, y: str(eval(x + y)), equation)
            )
            if equation_result == test_value:
                result += equation_result
                break
    return result


with open("2024/7/test") as file:
    assert (result := answer(file.read().splitlines())) == (
        expected := 3749
    ), f"Test sample: {result} is not {expected}"

with open("2024/7/data") as file:
    print(answer(file.read().splitlines()))
