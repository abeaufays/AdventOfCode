"""
Unknown:
a = times we need to push A
b = times we need to push B

Given:
Ax = Delta in x of button A
Ay = Delta in y of button A
Bx = Delta in x of button B
By = Delta in y of button B
Tx = x positon of Target
Ty = y positon of Target

We have the system:
| a*Ax + b*Bx = Tx
| a*Ay + b*By = Ty

We can express a as:
a = (Tx - b*Bx) / Ax

If we replace in second equation:
((Tx - b*Bx) / Ax)*Ay + b*By = Ty

We developp b until:
b = (Ty - (Ay/Ax)*Tx) / (-Bx*(Ay/Ax) + By)
then
a = (Tx - ((Ty - (Ay/Ax)*Tx) / (-Bx*(Ay/Ax) + By))*Bx) / Ax
"""

from decimal import Decimal


def part1(input: str) -> int:
    setups_str: list[str] = input.split("\n\n")
    result = 0
    for setup in setups_str:
        Ax, Ay, Bx, By, Tx, Ty = parse_setup(setup)
        b = (Ty - (Ay / Ax) * Tx) / (-Bx * (Ay / Ax) + By)
        a = (Tx - ((Ty - (Ay / Ax) * Tx) / (-Bx * (Ay / Ax) + By)) * Bx) / Ax

        if (round(a) * Ax + round(b) * Bx == Tx) and (
            round(a) * Ay + round(b) * By == Ty
        ):
            result += round(a) * 3 + round(b)
    return result


def part2(input: str) -> int:
    setups_str: list[str] = input.split("\n\n")
    result = 0
    for setup in setups_str:
        Ax, Ay, Bx, By, Tx, Ty = parse_setup(setup)
        Tx += 10000000000000
        Ty += 10000000000000
        b = (Ty - (Ay / Ax) * Tx) / (-Bx * (Ay / Ax) + By)
        a = (Tx - ((Ty - (Ay / Ax) * Tx) / (-Bx * (Ay / Ax) + By)) * Bx) / Ax

        if (round(a) * Ax + round(b) * Bx == Tx) and (
            round(a) * Ay + round(b) * By == Ty
        ):
            result += round(a) * 3 + round(b)
    return result


def parse_setup(setup: str):
    for line in setup.split("\n"):
        match line.split():
            case ["Button", "A:", Ax_raw, Ay_raw]:
                Ax = Decimal(Ax_raw[1:-1])
                Ay = Decimal(Ay_raw[1:])
            case ["Button", "B:", Bx_raw, By_raw]:
                Bx = Decimal(Bx_raw[1:-1])
                By = Decimal(By_raw[1:])
            case ["Prize:", Tx_raw, Ty_raw]:
                Tx = Decimal(Tx_raw[2:-1])
                Ty = Decimal(Ty_raw[2:])
            case _:
                raise ValueError
    return Ax, Ay, Bx, By, Tx, Ty


with open("2024/13/data") as file:
    file_content = file.read()
    print(part1(file_content))
    print(part2(file_content))
