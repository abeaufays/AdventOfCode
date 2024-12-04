import re


def answer(inp: str) -> int:
    expression = r"mul\((?P<left>\d{1,3})\,(?P<right>\d{1,3})\)"
    result = 0
    for match in re.finditer(expression, inp):
        result += int(match.group("left")) * int(match.group("right"))
    return result


assert (
    answer("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")
    == 161
), "test sample"
assert (
    answer("""xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]the
           n(mul(11,8)mul(8,5))""")
    == 161
), "test sample with multiline"


with open("2024/3/data") as file:
    print(answer(file.read()))
