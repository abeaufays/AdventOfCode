file = open("day9/data.txt", "r")


visited_position = set()
current_positions = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                     (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
# head_position = (0, 0)
# tail_position = (0, 0)

UP = (0, 1)
DOWN = (0, -1)
RIGHT = (1, 0)
LEFT = (-1, 0)

instructions_dict = {
    "U": UP,
    "D": DOWN,
    "R": RIGHT,
    "L": LEFT,

}


def add(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[int, int]:
    return (p1[0] + p2[0], p1[1] + p2[1])


def get_sign(x: int) -> int:
    if x == 0:
        return 0
    return int(x/abs(x))


def update_follower(tail: tuple[int, int], head: tuple[int, int]) -> tuple[int, int]:
    result = tail
    x_diff = head[0] - tail[0]
    y_diff = head[1] - tail[1]
    if abs(x_diff) > 1 or abs(y_diff) > 1:
        result = add(result, (get_sign(x_diff), get_sign(y_diff)))
    return result


def draw():
    tab = [["." for i in range(30)]for j in range(30)]
    for visited in visited_position:
        tab[visited[0]][visited[1]] = "#"
    tab[current_positions[0][0]][current_positions[0][1]] = "H"
    for i, pos in enumerate(current_positions[1:]):
        tab[pos[0]][pos[1]] = f"{i}"

    for line in tab:
        print("".join(line))


for line in file.readlines():
    instruction, step_numbers = line.split()
    step_numbers = int(step_numbers)
    for _ in range(step_numbers):
        print(current_positions)
        current_positions[0] = add(
            current_positions[0], instructions_dict[instruction])

        for i in range(len(current_positions) - 1):

            current_positions[i+1] = update_follower(
                current_positions[i+1], current_positions[i])
        visited_position.add(current_positions[-1])
        # draw()

print(len(visited_position))
