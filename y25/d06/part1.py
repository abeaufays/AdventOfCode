from functools import reduce


def answer(filename: str) -> int:
    with open(filename) as file:
        lines = file.readlines()

    equations_count = len(lines[0].split())

    equations = [[] for _ in range(equations_count)]
    for line in lines[:-1]:
        for index, number in enumerate(line.split()):
            equations[index].append(int(number))

    result = 0

    operation_mapper = {
        "*": lambda x,y: x*y,
        "+": lambda x,y: x+y,
    }
    for index, operation in enumerate(lines[-1].split()):
        result += reduce(operation_mapper[operation], equations[index])

    return result
