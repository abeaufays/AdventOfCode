import y25.d05.part2 as solution


def test_answer():
    assert solution.answer("y25/d05/test") == 14


class TestResolveRange:
    def test_merge_adjacent(self):
        assert solution.resolve_ranges([(1, 5), (3, 7), (10, 15)]) == {(1, 7), (10, 15)}

    def test_emcompassing_range_at_begining(self):
        assert solution.resolve_ranges([(1, 10), (2, 5), (6, 9)]) == {(1, 10)}

    def test_emcompassing_range_at_end(self):
        assert solution.resolve_ranges([(2, 5), (6, 9), (1, 10)]) == {(1, 10)}
