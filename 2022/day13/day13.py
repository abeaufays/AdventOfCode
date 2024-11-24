from functools import cmp_to_key

file = open("day13/data.txt")


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0
    elif isinstance(a, list) and isinstance(b, list):
        for x, y in zip(a, b):
            res = compare(x, y)
            if res != 0:
                return res
        if len(a) < len(b):
            return -1
        elif len(a) > len(b):
            return 1
        else:
            return 0
    else:
        if isinstance(a, int):
            return compare([a], b)
        else:
            return compare(a, [b])


assert compare([2, 3, 4], 4) == -1
assert compare([[1], [2, 3, 4]], [1, 1, 5, 1, 1]) == 1

# index = 1
# count = 0

# while True:
#     line1 = file.readline()
#     line2 = file.readline()
#     _ = file.readline()

#     if not line1:
#         break

#     left = eval(line1)
#     right = eval(line2)

#     is_in_right_order = compare(left, right)
#     print(is_in_right_order)
#     count += index if is_in_right_order else 0
#     index += 1

all_packets = []

for line in file.readlines():
    if "[" in line:
        all_packets.append(eval(line))

divider_packets_1 = [[2]]
divider_packets_2 = [[6]]

all_packets.append(divider_packets_1)
all_packets.append(divider_packets_2)


all_packets = sorted(all_packets, key=cmp_to_key(compare))
[print(packet) for packet in all_packets]

index_divider_1 = all_packets.index(divider_packets_1) + 1
index_divider_2 = all_packets.index(divider_packets_2) + 1

print(index_divider_1)
print(index_divider_2)
print(index_divider_1 * index_divider_2)
