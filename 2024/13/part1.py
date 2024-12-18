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

from decimal import Decimal, getcontext


def parse_setup(str): ...


# getcontext().prec = 10
Ax = Decimal(26)
Ay = Decimal(66)
Bx = Decimal(67)
By = Decimal(21)
Tx = Decimal(12748)
Ty = Decimal(12176)

b = (Ty - (Ay / Ax) * Tx) / (-Bx * (Ay / Ax) + By)
a = (Tx - ((Ty - (Ay / Ax) * Tx) / (-Bx * (Ay / Ax) + By)) * Bx) / Ax

print(a, b)
print(a % 1 == 0, b % 1 == 0)
print(round(a), round(b))
print(round(a) * Ax + round(b) * Bx)
print(round(a) * Ax + round(b) * Bx == Tx)


def test(result, expected):
    assert result == expected, f"{result} is not {expected}"
