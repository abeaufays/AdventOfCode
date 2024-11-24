def compute(inp: str) -> int:
    current_floor = 0
    for i, char in enumerate(inp):
        if char == "(":
            current_floor += 1
        if char == ")":
            current_floor -= 1
        if current_floor == -1:
            return i + 1
    return 0


assert compute(")") == 1
assert compute("()())") == 5

with open("2015/1/data.txt") as file:
    print(compute(file.readline()))
