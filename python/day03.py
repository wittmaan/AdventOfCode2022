import fileinput
import string
from collections import Counter
from functools import reduce
from operator import and_
from typing import List

# --- Day 3: Rucksack Reorganization ---
# --- Part one ---

sample_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".split(
    "\n"
)


class Compartment:
    def __init__(self, items: str):
        self.priorities = [string.ascii_letters.index(_) + 1 for _ in items]
        self.priority_count = Counter(self.priorities)


class Rucksack:
    def __init__(self, items, mode="part1"):
        self.mode = mode
        if mode == "part1":
            ind_half = int(len(items) / 2)
            self.compartments = [
                Compartment(items[ind_half:]),
                Compartment(items[:ind_half]),
            ]
        else:
            self.compartments = [
                Compartment(items[0]),
                Compartment(items[1]),
                Compartment(items[2]),
            ]

    def check(self):
        return list(reduce(and_, [_.priority_count for _ in self.compartments]))[0]


def calc_priority_sum(dat, mode="part1") -> int:
    dat = list(dat) if mode == "part2" else dat
    return sum([Rucksack(_, mode).check() for _ in dat])


assert calc_priority_sum(sample_input) == 157

puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = calc_priority_sum(puzzle_input)

assert solution_part1 == 8139
print(f"solution part1: {solution_part1}")


# --- Part two ---


def split_lines(dat: List[str], chunk_size=3):
    for i in range(0, len(dat), chunk_size):
        yield dat[i : i + chunk_size]


assert calc_priority_sum(split_lines(sample_input), mode="part2") == 70

solution_part2 = calc_priority_sum(split_lines(puzzle_input), mode="part2")
assert solution_part2 == 2668
print(f"solution part2: {solution_part2}")
