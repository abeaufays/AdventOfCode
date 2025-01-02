type Vec2D = tuple[int, int]


def add(a: Vec2D, b: Vec2D) -> Vec2D:
    return (a[0] + b[0], a[1] + b[1])


def sub(a: Vec2D, b: Vec2D) -> Vec2D:
    return (a[0] - b[0], a[1] - b[1])


def distance_manhattan(a: Vec2D, b: Vec2D) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
