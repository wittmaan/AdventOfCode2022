import fileinput
import operator
import re
from collections import deque
from dataclasses import dataclass
from functools import reduce
from typing import Deque, List, Union

# --- Day 11: Monkey in the Middle ---
# --- Part one ---

sample_input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
""".split(
    "\n"
)


@dataclass
class Operation:
    type: Union[operator.add, operator.mul]
    value: Union[str, int]


@dataclass
class TestType:
    divisible_by: int
    if_true: int
    if_false: int


class Monkey:
    def __init__(self, items, operation, test):
        self.items: Deque[int] = items
        self.operation = operation
        self.test: TestType = test
        self.inspected: int = 0


class MonkeyInTheMiddle:
    def __init__(self, dat: List[str]):
        self.monkeys: List[Monkey] = MonkeyInTheMiddle.fill(dat)

    @staticmethod
    def fill(dat: List[str]):
        monkeys: List[Monkey] = []
        items = operation = divisible_by = if_true = if_false = None
        for line in dat:
            if "Starting items" in line:
                items = [int(_) for _ in re.findall("\d+", line)]
            elif "Operation" in line:
                tmp = line.split()
                if tmp[4] == "*":
                    op = operator.mul
                elif tmp[4] == "+":
                    op = operator.add
                else:
                    raise ValueError(f"unkonwn operator {tmp[4]}")
                if tmp[5] == "old":
                    val = tmp[5]
                else:
                    val = int(tmp[5])
                operation = Operation(op, val)
            elif "Test" in line:
                divisible_by = int(line.split()[-1])
            elif "If true" in line:
                if_true = int(line.split()[-1])
            elif "If false" in line:
                if_false = int(line.split()[-1])

            if all(_ is not None for _ in [items, operation, divisible_by, if_true, if_false]):
                monkeys.append(Monkey(deque(items), operation, TestType(divisible_by, if_true, if_false),))
                items = operation = divisible_by = if_true = if_false = None

        return monkeys

    def play(self, rounds=20, mode="part1"):
        if mode == "part1":
            for _ in range(rounds):
                self.play_round()
        else:
            modulo = reduce(operator.mul, [monkey.test.divisible_by for monkey in self.monkeys])
            for _ in range(rounds):
                self.play_round(modulo)

        inspected = sorted([_.inspected for _ in self.monkeys])
        return inspected[-1] * inspected[-2]

    def play_round(self, modulo=None):
        for monkey in self.monkeys:
            while monkey.items:
                item = monkey.items.popleft()
                item = MonkeyInTheMiddle.inspect(item, monkey)
                if modulo is not None:
                    item = MonkeyInTheMiddle.reduce_worry(item, operator.mod, modulo)
                else:
                    item = MonkeyInTheMiddle.reduce_worry(item, operator.floordiv, 3)
                target = MonkeyInTheMiddle.throw_to_target(item, monkey.test)
                self.monkeys[target].items.append(item)

    @staticmethod
    def inspect(item, monkey):
        if type(monkey.operation.value) is str:
            item = monkey.operation.type(item, item)
        else:
            item = monkey.operation.type(item, monkey.operation.value)
        monkey.inspected += 1
        return item

    @staticmethod
    def reduce_worry(item: int, operation: Union[operator.floordiv, operator.mod], value: int = 3) -> int:
        return operation(item, value)

    @staticmethod
    def throw_to_target(item, test: TestType):
        return test.if_true if (item % test.divisible_by) == 0 else test.if_false


assert MonkeyInTheMiddle(sample_input).play() == 10605

puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = MonkeyInTheMiddle(puzzle_input).play()

assert solution_part1 == 182293
print(f"solution part1: {solution_part1}")


# --- Part two ---

solution_part2 = MonkeyInTheMiddle(puzzle_input).play(rounds=10000, mode="part2")

assert solution_part2 == 54832778815
print(f"solution part2: {solution_part2}")
