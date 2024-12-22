import re


# [S]                 [T] [Q]
# [L]             [B] [M] [P]     [T]
# [F]     [S]     [Z] [N] [S]     [R]
# [Z] [R] [N]     [R] [D] [F]     [V]
# [D] [Z] [H] [J] [W] [G] [W]     [G]
# [B] [M] [C] [F] [H] [Z] [N] [R] [L]
# [R] [B] [L] [C] [G] [J] [L] [Z] [C]
# [H] [T] [Z] [S] [P] [V] [G] [M] [M]
#  1   2   3   4   5   6   7   8   9

crate_stacks = [
    None,
    ['H', 'R', 'B', 'D', 'Z', 'F', 'L', 'S'],
    ['T', 'B', 'M', 'Z', 'R'],
    ['Z', 'L', 'C', 'H', 'N', 'S'],
    ['S', 'C', 'F', 'J'],
    ['P', 'G', 'H', 'W', 'R', 'Z', 'B'],
    ['V', 'J', 'Z', 'G', 'D', 'N', 'M', 'T'],
    ['G', 'L', 'N', 'W', 'F', 'S', 'P', 'Q'],
    ['M', 'Z', 'R'],
    ['M', 'C', 'L', 'G', 'V', 'R', 'T']
]

# test data :
# crate_stacks = [
#     None,
#     ['Z', 'N', ],
#     ['M', 'C', 'D'],
#     ['P']
# ]


verbose = False

file = open("day5/data.txt", "r")

if verbose:
    [print(stack) for stack in crate_stacks]

for line_number, line in enumerate(file.readlines()):
    match = re.match(
        r"move (?P<amount>\d+) from (?P<from>\d) to (?P<to>\d)", line)

    amount = int(match.group("amount"))
    from_ = int(match.group("from"))
    to = int(match.group("to"))

    if verbose:
        print("line", line_number)
        [print(i, stack) for i, stack in enumerate(crate_stacks)]
        print(f"amount: {amount} / from: {from_} / to: {to}")
        print(" ---> ")

    # for i in range(amount):
    #     crate = crate_stacks[from_].pop()
    #     crate_stacks[to].append(crate)

    crates = crate_stacks[from_][-amount:]
    crate_stacks[to].extend(crates)
    del crate_stacks[from_][-amount:]


[print(stack) for stack in crate_stacks]

print("".join(stack[-1] for stack in crate_stacks[1:]))
