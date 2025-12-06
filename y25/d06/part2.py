from functools import reduce


def answer(filename: str) -> int:
    with open(filename) as file:
        lines = file.readlines()

    operation_mapper = {
        "*": lambda x, y: x * y,
        "+": lambda x, y: x + y,
    }

    logger = {"*":0, "+":0}

    result = 0
    current_equation: list[int] = []
    for col in range(len(lines[0])):
        if lines[-1][col] != " ": # On last column it will be a \n
            if current_equation:
                result += reduce(operation_mapper[current_operation], current_equation)
                current_equation = []
            current_operation = lines[-1][col]

        current_number = ""
        for line in lines[:-1]:
            current_number += line[col]
        if current_number.strip():
            current_equation.append(int(current_number.strip()))

    return result
