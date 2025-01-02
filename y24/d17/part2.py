from __future__ import annotations
from dataclasses import dataclass
from functools import partial


@dataclass
class Device:
    def __init__(self, registers: list[int]):
        self.registers: list[int] = registers
        self.output: list[int] = []

    def run(self):
        A, B, C = self.registers
        B = A % 8
        B = B ^ 3
        C = A // (2**B)
        B = B ^ C
        A = A // 8
        B = B ^ 5
        self.output.append(B % 8)
        self.registers = [A, B, C]

    def read_output(self) -> str:
        return ",".join(map(str, self.output))


def parse(input_: str) -> tuple[list[int], list[int]]:
    registers = [-1, -1, -1]
    for line in input_.splitlines():
        match line.split():
            case ["Register", register_raw, value]:
                registers[{"A": 0, "B": 1, "C": 2}[register_raw[0]]] = int(value)
            case ["Program:", program_raw]:
                program = list(map(int, program_raw.split(",")))
    return registers, program


def answer_part1(filename: str) -> str:
    with open(filename) as file:
        registers, program = parse(file.read())
        device = Device(registers)
        while device.registers[0] != 0:
            device.run()

    return device.read_output()


def get_output_for_register(register: int) -> list[int]:
    registers = [register, 0, 0]
    device = Device(registers)
    while device.registers[0] != 0:
        device.run()
    return device.output


def octal_digits_list_to_int(octal_digits: list[int], expected_len: int) -> int:
    """Takes highest weight digits firsts"""
    return int("".join((map(str, octal_digits))).ljust(expected_len, "0"), 8)


def answer(filename: str) -> int:
    octal_digits = [1]

    with open(filename) as file:
        _, program = parse(file.read())
        found = False
        i = 0
        to_int = partial(octal_digits_list_to_int, expected_len=len(program))
        while not found:
            output = get_output_for_register(to_int(octal_digits))
            if output[-(i + 1)] == program[-(i + 1)]:
                if len(octal_digits) == len(program):
                    return to_int(octal_digits)
                i += 1
                octal_digits.append(0)
            octal_digits[i] += 1
            while octal_digits[i] >= 8:
                octal_digits.pop()
                i -= 1
                octal_digits[i] += 1
    return 0
