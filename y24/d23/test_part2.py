import y24.d23.part2 as solution


def test_answer():
    assert solution.answer("y24/d23/test") == "co,de,ka,ta"


class TestConnection:
    def test_hash(self):
        a = solution.Group((1, 2, 8))
        b = solution.Group((2, 8, 1))
        c = solution.Group((1, 2, 7))

        assert hash(a) == hash(b)
        assert not (hash(c) == hash(b))

    def test_eq(self):
        a = solution.Group((1, 2, 8))
        b = solution.Group((2, 8, 1))
        c = solution.Group((1, 2, 7))

        assert a == b
        assert not (c == a)


def test_get_all_triple_connection():
    graph = solution.parse_file("y24/d23/test")
    triple_connections = solution.get_all_triple_connection(graph)

    assert triple_connections == {
        solution.Group(("aq", "cg", "yn")),
        solution.Group(("aq", "vc", "wq")),
        solution.Group(("co", "de", "ka")),
        solution.Group(("co", "de", "ta")),
        solution.Group(("co", "ka", "ta")),
        solution.Group(("de", "ka", "ta")),
        solution.Group(("kh", "qp", "ub")),
        solution.Group(("qp", "td", "wh")),
        solution.Group(("tb", "vc", "wq")),
        solution.Group(("tc", "td", "wh")),
        solution.Group(("td", "wh", "yn")),
        solution.Group(("ub", "vc", "wq")),
    }


def test_find_bigger_groups():
    graph = {
        "a": ["b", "c", "d", "e"],
        "b": ["a", "c"],
        "c": ["a", "b", "d"],
        "d": ["a", "c"],
        "e": ["a"],
    }
    assert solution.find_bigger_groups(solution.Group(("a", "b")), graph) == (
        True,
        [solution.Group(("a", "b", "c"))],
    )
    assert solution.find_bigger_groups(solution.Group(("a", "b", "c")), graph) == (
        False,
        [],
    )
