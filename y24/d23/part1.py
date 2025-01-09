from collections import defaultdict


class Connection:
    def __init__(self, elements: tuple):
        self.elements = elements

    def __eq__(self, value):
        return sorted(self.elements) == sorted(value.elements)

    def __hash__(self):
        return hash(tuple(sorted(self.elements)))


def get_all_triple_connection(graph: dict[str, list[str]]):
    result = set()
    for first_element in graph.keys():
        for second_element in graph[first_element]:
            for third_element in graph[second_element]:
                if first_element in graph[third_element]:
                    result.add(
                        Connection((first_element, second_element, third_element))
                    )

    return result


def parse_file(filename: str) -> dict[str, list[str]]:
    graph: dict[str, list[str]] = defaultdict(list)

    with open(filename) as file:
        lines = file.read().splitlines()
        for line in lines:
            a, b = line.split("-")
            graph[a].append(b)
            graph[b].append(a)

    return graph


def answer(filename: str) -> int:
    graph = parse_file(filename)
    connections = get_all_triple_connection(graph)
    return sum(
        1
        for connection in connections
        if any([element[0] == "t" for element in connection.elements])
    )
