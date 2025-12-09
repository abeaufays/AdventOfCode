def answer(filename: str) -> int:
    positions = []
    with open(filename) as file:
        for line in file:
            positions.append(tuple(map(int, line.split(","))))

    largest_area = 0
    for index, first_position in enumerate(positions):
        for second_position in positions[index + 1 :]:
            current_area = (abs(second_position[0] - first_position[0]) + 1) * (
                abs(second_position[1] - first_position[1]) + 1
            )
            if current_area > largest_area:
                largest_area = current_area

    return largest_area
