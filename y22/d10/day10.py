file = open("day10/data.txt", "r")

cycle_count = 0
register = 1
signal_strenght_sum = 0
all_lines = []
current_line = ""


def cycle_process():
    global cycle_count
    global register
    global signal_strenght_sum
    global current_line

    cycle_count += 1
    current_line += "#" if register <= cycle_count % 40 <= register + 2 else "."

    if (cycle_count-20) % 40 == 0:
        signal_strenght_sum += register * cycle_count

    if cycle_count % 40 == 0:
        all_lines.append(current_line)
        current_line = ""
    print(f"{cycle_count} - {register} - {signal_strenght_sum} ")


for line_number, line in enumerate(file.readlines()):
    match line.split():
        case ["noop"]:
            cycle_process()
        case ["addx", value]:
            cycle_process()
            cycle_process()
            register += int(value)
        case _:
            assert False


print(signal_strenght_sum)
for line in all_lines:
    print(line)
