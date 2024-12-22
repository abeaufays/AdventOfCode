from __future__ import annotations
import functools


def answer(input_: str):
    page_ordering_rules_input, updates_input = input_.split("\n\n")

    page_ordering_rules: list[tuple] = _compute_rules(page_ordering_rules_input)

    result = 0

    for update in (
        list(map(int, update_raw.split(",")))
        for update_raw in updates_input.split("\n")
    ):
        if not _is_update_ordered(update, page_ordering_rules):
            ordered_update = _order(update, page_ordering_rules)
            result += _get_middle(ordered_update)

    return result


def _item_order_validity(a: int, b: int, rules: list[tuple[int, int]]) -> int:
    for left, right in rules:
        if {a, b} == {left, right}:
            return -1 if a == left else 1
    return 0


def _order(update: list[int], rules: list[tuple[int, int]]) -> list[int]:
    return sorted(
        update,
        key=functools.cmp_to_key(functools.partial(_item_order_validity, rules=rules)),
    )


def _is_update_ordered(update: list[int], rules: list[tuple[int, int]]) -> bool:
    return update == _order(update, rules)


def tests():
    rules = [(1, 2)]
    assert _item_order_validity(1, 2, rules) == -1
    assert _item_order_validity(2, 1, rules) == 1
    assert _item_order_validity(4, 5, rules) == 0
    rules = [(1, 2), (2, 3)]
    assert _is_update_ordered([1, 2, 3], rules)
    assert not _is_update_ordered([1, 3, 2], rules)


tests()


def _compute_rules(input_: str) -> list[tuple]:
    return [tuple(map(int, line.split("|"))) for line in input_.split("\n")]


def _get_middle(update: list[int]) -> int:
    return update[len(update) // 2]


with open("2024/5/test") as file:
    assert (result := answer(file.read())) == (
        expected := 123
    ), f"`Test sample: {result} is not {expected}"


with open("2024/5/data") as file:
    print(answer(file.read()))
