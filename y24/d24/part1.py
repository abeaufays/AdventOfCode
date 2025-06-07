from functools import cache
from io import TextIOWrapper

GATES = {
    "XOR": lambda a, b: a ^ b,
    "AND": lambda a, b: a and b,
    "OR": lambda a, b: a or b,
}


@cache
def access(register: str) -> bool:
    global data
    return data[register]()


def parse_file(input_: TextIOWrapper):
    initial_raw, instructions_raw = input_.read().split("\n\n")
    global data
    data = dict()

    for line in initial_raw.splitlines():
        register_raw, value_raw = line.split()
        data[register_raw[:-1]] = lambda x=value_raw: x == "1"

    for line in instructions_raw.splitlines():
        input_1, gate, input_2, _, output = line.split()
        data[output] = lambda a=input_1, b=input_2, gate=gate: GATES[gate](
            access(a), access(b)
        )

    return data


def answer(filename: str) -> int:
    with open(filename) as file:
        data = parse_file(file)

    result = ""
    i = 0
    while (register := "z" + str(i).zfill(2)) in data.keys():
        result = ("1" if access(register) else "0") + result
        i += 1

    return int(result, 2)
