file = open("day4/data.txt", "r")

number_of_selfcontaining_pair = 0
number_of_overlapping_pair = 0

for line in file.readlines():
    a, b = line.split(",")
    a_lower, a_upper = map(int, a.split("-"))
    b_lower, b_upper = map(int, b.split("-"))

    is_selfcontaining_pair = (a_lower <= b_lower and a_upper >= b_upper) or (
        a_lower >= b_lower and a_upper <= b_upper)

    is_overlapping_pair = (a_lower <= b_lower <= a_upper) or (a_lower <= b_upper <= a_upper) or (
        b_lower <= a_lower <= b_upper) or (b_lower <= a_upper <= b_upper)

    print(f"{a_lower} {a_upper} - {b_lower} {b_upper} {is_overlapping_pair}")

    if is_selfcontaining_pair:
        number_of_selfcontaining_pair += 1

    if is_overlapping_pair:
        number_of_overlapping_pair += 1

print(number_of_overlapping_pair)
