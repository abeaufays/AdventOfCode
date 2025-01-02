from dataclasses import dataclass

A = 0
B = 1
C = 2


@dataclass
class Device:
    def __init__(self, registers: list[int], program: list[int]):
        self.registers: list[int] = registers
        self.program: list[int] = program
        self.output: list[int] = []
        self.instruction_pointer: int = 0

    def run(self):
        instruction, operand = self.program[
            self.instruction_pointer : self.instruction_pointer + 2
        ]
        self.OPCODE_MAPPING[instruction](self, operand)

    def read_output(self) -> str:
        return ",".join(map(str, self.output))

    def combo_operand(self, operand: int) -> int:
        return [
            0,
            1,
            2,
            3,
            self.registers[A],
            self.registers[B],
            self.registers[C],
            None,
        ][operand] or -1

    def litteral_operand(self, operand: int) -> int:
        return operand

    def update_instruction_pointer(self):
        self.instruction_pointer += 2

    def adv(self, operand: int):
        self.registers[A] = int(self.registers[A] // 2 ** self.combo_operand(operand))
        self.update_instruction_pointer()

    def bxl(self, operand: int):
        self.registers[B] = self.registers[B] ^ self.litteral_operand(operand)
        self.update_instruction_pointer()

    def bst(self, operand: int):
        self.registers[B] = self.combo_operand(operand) % 8
        self.update_instruction_pointer()

    def jnz(self, operand: int):
        if self.registers[A] != 0:
            self.instruction_pointer = self.litteral_operand(operand)
        else:
            self.update_instruction_pointer()

    def bxc(self, operand: int):
        print(type(self.registers[B]), type(self.registers[C]))
        self.registers[B] = self.registers[B] ^ self.registers[C]
        self.update_instruction_pointer()

    def out(self, operand: int):
        self.output.append(self.combo_operand(operand) % 8)
        self.update_instruction_pointer()

    def bdv(self, operand: int):
        self.registers[B] = int(self.registers[A] // 2 ** self.combo_operand(operand))
        self.update_instruction_pointer()

    def cdv(self, operand: int):
        self.registers[C] = int(self.registers[A] // 2 ** self.combo_operand(operand))
        self.update_instruction_pointer()

    OPCODE_MAPPING = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]


def parse(input_: str) -> Device:
    registers = [-1, -1, -1]
    for line in input_.splitlines():
        match line.split():
            case ["Register", register_raw, value]:
                registers[{"A": A, "B": B, "C": C}[register_raw[0]]] = int(value)
            case ["Program:", program_raw]:
                program = list(map(int, program_raw.split(",")))
    return Device(registers, program)


def answer(filename: str) -> str:
    with open(filename) as file:
        device = parse(file.read())
        program_len = len(device.program)
        while device.instruction_pointer < program_len:
            device.run()

    return device.read_output()


print(answer("y24/d17/data"))
