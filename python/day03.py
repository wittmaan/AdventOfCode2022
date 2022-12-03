import fileinput
from typing import List
import string
from collections import Counter

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
    def __init__(self, items: str):
        ind_half = int(len(items) / 2)
        self.compartments = [
            Compartment(items[ind_half:]),
            Compartment(items[:ind_half]),
        ]

    def check(self):
        both_priorities = (
            self.compartments[0].priority_count & self.compartments[1].priority_count
        )
        return list(both_priorities.keys())[0]


def calc_priority_sum(dat: List[str]) -> int:
    return sum([Rucksack(_).check() for _ in dat])


assert calc_priority_sum(sample_input) == 157

puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = calc_priority_sum(puzzle_input)

assert solution_part1 == 8139
print(f"solution part1: {solution_part1}")


# --- Part two ---

# assert calc_total_score(sample_input, mode="part2") == 12
# solution_part2 = calc_total_score(puzzle_input, mode="part2")
#
# assert solution_part2 == 13889
# print(f"solution part2: {solution_part2}")
