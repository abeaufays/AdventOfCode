from __future__ import annotations
from collections import defaultdict


def answer(input_: str):
    page_ordering_rules_input, updates_input = input_.split("\n\n")

    page_ordering_rules: dict[int, set[int]] = _compute_rules(page_ordering_rules_input)

    result = 0

    for update in (
        list(map(int, update_raw.split(",")))
        for update_raw in updates_input.split("\n")
    ):
        forbidden_product: set[int] = set()
        is_valid = True
        for page in update:
            if page in forbidden_product:
                is_valid = False
                break
            rule = page_ordering_rules[page]
            forbidden_product = forbidden_product.union(rule)
        if is_valid:
            middle = update[len(update) // 2]
            result += middle
    return result


def _compute_rules(input_: str) -> dict[int, set[int]]:
    lines = input_.split("\n")
    rule_dict: dict[int, set[int]] = defaultdict(set)

    for line in lines:
        left, right = map(int, line.split("|"))
        rule_dict[right].add(left)

    return rule_dict


with open("2024/5/test") as file:
    assert (result := answer(file.read())) == (
        expected := 143
    ), f"Test sample: {result} is not {expected}"


with open("2024/5/data") as file:
    print(answer(file.read()))
