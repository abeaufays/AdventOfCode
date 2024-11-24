def compute(inp: str) -> int:
    return inp.count("(") - inp.count(")")


assert compute("(())") == 0
assert compute("))(((((") == 3
assert compute("())") == -1
assert compute(")())())") == -3
assert compute("()()") == 0
assert compute(")))") == -3

with open("2015/1/data.txt") as file:
    print(compute(file.readline()))
