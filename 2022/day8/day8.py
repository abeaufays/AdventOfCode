file = open("day8/data.txt", "r")

data = [[*map(int, line[:-1])] for line in file.readlines()]

for line in data:
    print(line)


width = len(data[0])
height = len(data)


def compute_tree_grid_visibility(data):
    is_visible = [[False for j in range(width)] for i in range(height)]

    # left to right
    for i in range(height):
        max_tree_height = -1
        for j in range(width):
            if data[i][j] > max_tree_height:
                is_visible[i][j] = True
                max_tree_height = data[i][j]

    # right to left
    for i in range(height):
        max_tree_height = -1
        for j in range(width)[::-1]:
            if data[i][j] > max_tree_height:
                is_visible[i][j] = True
                max_tree_height = data[i][j]

    # top to bottom
    for i in range(width):
        max_tree_height = -1
        for j in range(height):
            if data[j][i] > max_tree_height:
                is_visible[j][i] = True
                max_tree_height = data[j][i]

    # bottom to top
    for i in range(width):
        max_tree_height = -1
        for j in range(height)[::-1]:
            if data[j][i] > max_tree_height:
                is_visible[j][i] = True
                max_tree_height = data[j][i]

    return is_visible


def compute_cell_visibility(data, x: int, y: int):
    if x == 0 or y == 0 or x == width-1 or y == height-1:
        return 0

    current_tree_height = data[y][x]

    left_to_right_count = 0
    for i in range(x+1, width):
        left_to_right_count += 1
        if data[y][i] >= current_tree_height:
            break

    right_to_left_count = 0
    for i in range(x)[::-1]:
        right_to_left_count += 1
        if data[y][i] >= current_tree_height:
            break

    top_to_bottom_count = 0
    for i in range(y+1, height):
        top_to_bottom_count += 1
        if data[i][x] >= current_tree_height:
            break

    bottom_to_top_count = 0
    for i in range(y)[::-1]:
        bottom_to_top_count += 1
        if data[i][x] >= current_tree_height:
            break

    return left_to_right_count * right_to_left_count * top_to_bottom_count * bottom_to_top_count


# print(compute_cell_visibility(data, 2, 3))


# print(data)
# print(width)
# print(height)

# print(sum(sum(1 for i in line if i) for line in is_visible))

print(max(compute_cell_visibility(data, x, y)
          for x in range(height) for y in range(width)))
