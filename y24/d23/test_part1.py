import y24.d23.part1 as solution


def test_answer():
    assert solution.answer("y24/d23/test") == 7


class TestConnection:
    def test_hash(self):
        a = solution.Connection((1, 2, 8))
        b = solution.Connection((2, 8, 1))
        c = solution.Connection((1, 2, 7))

        assert hash(a) == hash(b)
        assert not (hash(c) == hash(b))

    def test_eq(self):
        a = solution.Connection((1, 2, 8))
        b = solution.Connection((2, 8, 1))
        c = solution.Connection((1, 2, 7))

        assert a == b
        assert not (c == a)


def test_get_all_triple_connection():
    graph = solution.parse_file("y24/d23/test")
    triple_connections = solution.get_all_triple_connection(graph)

    assert triple_connections == {
        solution.Connection(("aq", "cg", "yn")),
        solution.Connection(("aq", "vc", "wq")),
        solution.Connection(("co", "de", "ka")),
        solution.Connection(("co", "de", "ta")),
        solution.Connection(("co", "ka", "ta")),
        solution.Connection(("de", "ka", "ta")),
        solution.Connection(("kh", "qp", "ub")),
        solution.Connection(("qp", "td", "wh")),
        solution.Connection(("tb", "vc", "wq")),
        solution.Connection(("tc", "td", "wh")),
        solution.Connection(("td", "wh", "yn")),
        solution.Connection(("ub", "vc", "wq")),
    }
