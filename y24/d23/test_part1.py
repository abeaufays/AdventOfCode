import y24.d23.part1 as solution


def test_answer():
    assert solution.answer("y24/d23/test") == 7


class TestConnection:
    def test_hash(self):
        a = solution.Connection(1, 2)
        b = solution.Connection(2, 1)

        assert hash(a) == hash(b)

    def test_eq(self):
        a = solution.Connection(1, 2)
        b = solution.Connection(2, 1)

        assert a == b


def test_graph():
    graph = set()

    graph.add(solution.Connection(1, 2))

    assert solution.Connection(2, 1) in graph
