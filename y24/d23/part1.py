class Connection:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, value):
        return min(self.a, self.b) == min(value.a, value.b) and max(
            self.a, self.b
        ) == max(value.a, value.b)

    def __hash__(self):
        return hash((min(self.a, self.b), max(self.a, self.b)))


def parse_file(filename: str) -> set[Connection]:
    graph: set[Connection] = set()
    with open(filename) as file:
        lines = file.read().splitlines()
        for line in lines:
            a, b = line.split("-")
            connection = Connection(a, b)
            graph.add(connection)

    return graph


def answer(filename: str) -> int:
    return 0
