from typing import Callable


class Monkey:
    def __init__(self, starting_items: list[int], operation: Callable, test_value: int) -> None:
        self.items = starting_items
        self.operation = operation
        self.test_value = test_value
        self.if_true = None
        self.if_false = None
        self.inspecting_counter = 0

    def process_turn(self):
        for _ in range(len(self.items)):
            self.inspecting_counter += 1

            item = self.items.pop(0)

            item = self.operation(item) % 9699690

            # item = item // 3

            if item % self.test_value == 0:
                self.if_true.items.append(item)
            else:
                self.if_false.items.append(item)


monkey0 = Monkey([71, 56, 50, 73], lambda old: old * 11, 13)
monkey1 = Monkey([70, 89, 82], lambda old: old + 1, 7)
monkey2 = Monkey([52, 95], lambda old: old * old, 3)
monkey3 = Monkey([94, 64, 69, 87, 70], lambda old: old + 2, 19)
monkey4 = Monkey([98, 72, 98, 53, 97, 51], lambda old: old + 6, 5)
monkey5 = Monkey([79], lambda old: old + 7, 2)
monkey6 = Monkey([77, 55, 63, 93, 66, 90, 88, 71], lambda old: old * 7, 11)
monkey7 = Monkey([54, 97, 87, 70, 59, 82, 59], lambda old: old + 8, 17)

monkey0.if_true = monkey1
monkey0.if_false = monkey7

monkey1.if_true = monkey3
monkey1.if_false = monkey6

monkey2.if_true = monkey5
monkey2.if_false = monkey4

monkey3.if_true = monkey2
monkey3.if_false = monkey6

monkey4.if_true = monkey0
monkey4.if_false = monkey5

monkey5.if_true = monkey7
monkey5.if_false = monkey0

monkey6.if_true = monkey2
monkey6.if_false = monkey4

monkey7.if_true = monkey1
monkey7.if_false = monkey3

all_monkeys = [monkey0,    monkey1,    monkey2,    monkey3,
               monkey4,    monkey5,    monkey6,    monkey7]

for round in range(10000):
    print(round)
    for monkey in all_monkeys:
        monkey.process_turn()

print([monkey.inspecting_counter for monkey in all_monkeys])

top2, top1 = sorted([monkey.inspecting_counter for monkey in all_monkeys])[-2:]
print(top1 * top2)
