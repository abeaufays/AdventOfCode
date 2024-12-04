import re


def answer(inp: str) -> int:
    expression = r"(?P<mul>mul\((?P<left>\d{1,3})\,(?P<right>\d{1,3})\))|(?P<do>do\(\))|(?P<dont>don't\(\))"

    result = 0
    enabled = True
    for match in re.finditer(expression, inp):
        if enabled and match.groupdict().get("mul"):
            result += int(match.groupdict().get("left")) * int(
                match.groupdict().get("right")
            )
        elif match.groupdict().get("do"):
            enabled = True
        elif match.groupdict().get("dont"):
            enabled = False
    return result


assert (
    result := answer(
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    )
) == (expected := 48), f"Sample: {result} is not {expected}"


with open("2024/3/data") as file:
    print(answer(file.read()))
