file = open("day12/data.txt", "r")


def get_adjacent_list(pos, height, width):
    adjacent = [
        (pos[0], pos[1] + 1),
        (pos[0], pos[1] - 1),
        (pos[0] + 1, pos[1]),
        (pos[0] - 1, pos[1]),
    ]
    return filter(lambda pos: 0 <= pos[0] < height
                  and 0 <= pos[1] < width, adjacent)


assert (-1, 0) not in get_adjacent_list((0, 0), 15, 15)


def init(file):
    data = [list(map(ord, line[:-1]))for line in file.readlines()]
    all_minimum_height_pos = []
    [print(line) for line in data]

    height = len(data)
    width = len(data[0])

    start = None
    end = None
    for line_index, line in enumerate(data):
        col_index = -1
        while ord("a") in line[col_index+1:]:
            col_index = line.index(ord("a"), col_index+1)
            if not all(map(lambda pos: data[pos[0]][pos[1]] == ord("a"), get_adjacent_list((line_index, col_index), height, width))):
                all_minimum_height_pos.append((line_index, col_index))

        if ord("S") in line:
            col_index = line.index(ord("S"))
            start = (line_index, col_index)
            data[line_index][col_index] = ord('a')

        if ord("E") in line:
            col_index = line.index(ord("E"))
            end = (line_index, col_index)
            data[line_index][col_index] = ord('z')

        if start != None and end != None:
            break

    assert start != None
    assert end != None

    return data, start, end, height, width, all_minimum_height_pos


data, start, end, height, width, all_minimum_height_pos = init(file)


def find_shortest_path(start):
    global data
    global end
    global height
    global width

    current_pos = start
    step_count = 0

    visited_pos = [start]

    current_buffer = [start]
    next_buffer = []

    while True:
        if not current_buffer:
            current_buffer = next_buffer
            next_buffer = []
            step_count += 1

        try:
            current_pos = current_buffer.pop(0)
        except:
            return 1e8

        if current_pos == end:
            break

        current_height = data[current_pos[0]][current_pos[1]]

        possible_nexts = get_adjacent_list(current_pos, height, width)

        for possible_next in possible_nexts:
            if possible_next in visited_pos:
                continue

            possible_next_height = data[possible_next[0]][possible_next[1]]
            if possible_next_height <= current_height + 1 and possible_next_height != ord("a"):
                next_buffer.append(possible_next)
                visited_pos.append(possible_next)
        pass
    return step_count


print(len(all_minimum_height_pos))
steps = []
for i, pos in enumerate(all_minimum_height_pos):
    print(i)
    steps.append(find_shortest_path(pos))

print(find_shortest_path(start))
print(min(steps))
