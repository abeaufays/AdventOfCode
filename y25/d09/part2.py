def is_in_between(a, b, x) -> bool:
    xmin, xmax = min(a[0], b[0]), max(a[0], b[0])
    ymin, ymax = min(a[1], b[1]), max(a[1], b[1])
    return xmin < x[0] < xmax and ymin < x[1] < ymax


def answer(filename: str) -> int:
    positions = []
    with open(filename) as file:
        for line in file:
            positions.append(tuple(map(int, line.split(","))))

    landmarks = []
    for p1, p2 in zip(positions[:-1], positions[1:]):
        landmarks.append(p1)
        landmarks.append(((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2))
    landmarks.append(positions[-1])

    largest_area = 0
    for index, first_position in enumerate(positions):
        for second_position in positions[index + 1 :]:
            current_area = (abs(second_position[0] - first_position[0]) + 1) * (
                abs(second_position[1] - first_position[1]) + 1
            )
            if current_area > largest_area and not any(
                is_in_between(first_position, second_position, other_position)
                for other_position in landmarks
            ):
                largest_area = current_area

    return largest_area
