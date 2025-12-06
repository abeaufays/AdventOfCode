from functools import reduce


def answer(filename: str) -> int:
    with open(filename) as file:
        lines = file.readlines()

    equations_count = len(lines[0].split())

    equations = [[] for _ in range(equations_count)]
    for line in lines[:-1]:
        for equation_index, number in enumerate(line.split()):
            equations[equation_index].append(str(number))


    processed_equations = []
    for equation_index in range(equations_count):
        raw_numbers = equations[equation_index]
        still_has_digits_to_process = True
        processed_numbers = []
        while still_has_digits_to_process:
            still_has_digits_to_process = False
            current_processed_number_str = ""
            for raw_number_index in range(len(raw_numbers)):
                if raw_numbers[raw_number_index]:
                    still_has_digits_to_process = True
                    current_processed_number_str += raw_numbers[raw_number_index][0]
                    raw_numbers[raw_number_index] = raw_numbers[raw_number_index][1:]
            if current_processed_number_str:
                processed_numbers.append(int(current_processed_number_str))
        processed_equations.append(processed_numbers)
        print(processed_numbers)

    result = 0

    operation_mapper = {
        "*": lambda x,y: x*y,
        "+": lambda x,y: x+y,
    }
    for equation_index, operation in enumerate(lines[-1].split()):
        result += reduce(operation_mapper[operation], processed_equations[equation_index])

    return result
