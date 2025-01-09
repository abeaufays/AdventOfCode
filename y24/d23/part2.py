from collections import defaultdict


type Graph = dict[str, set[str]]


class Group:
    def __init__(self, elements: tuple):
        self.elements = elements

    def __eq__(self, value):
        return sorted(self.elements) == sorted(value.elements)

    def __hash__(self):
        return hash(tuple(sorted(self.elements)))


def get_all_triple_connection(graph: Graph) -> set[Group]:
    result = set()
    for first_element in graph.keys():
        for second_element in graph[first_element]:
            for third_element in graph[second_element]:
                if first_element in graph[third_element]:
                    result.add(Group((first_element, second_element, third_element)))

    return result


def can_add(group: Group, element: str, graph: Graph) -> bool:
    for current_group_element in group.elements:
        if element not in graph[current_group_element]:
            return False
    return True


def find_bigger_groups(start: Group, graph: Graph) -> tuple[bool, list[Group]]:
    results = []
    found = False
    for element in graph.keys():
        if can_add(start, element, graph):
            found = True
            results.append(Group((*start.elements, (element))))
    return (found, results)


def parse_file(filename: str) -> Graph:
    graph: Graph = defaultdict(set)

    with open(filename) as file:
        lines = file.read().splitlines()
        for line in lines:
            a, b = line.split("-")
            graph[a].add(b)
            graph[b].add(a)

    return graph


def answer(filename: str) -> str:
    graph = parse_file(filename)
    buffer = get_all_triple_connection(graph)
    biggest_group = Group(())
    while buffer:
        group = buffer.pop()
        found, groups = find_bigger_groups(group, graph)
        if found:
            buffer.update(groups)
        elif len(group.elements) > len(biggest_group.elements):
            biggest_group = group

    return ",".join(sorted(biggest_group.elements))


# Executed in 274.04926347732544 seconds.
