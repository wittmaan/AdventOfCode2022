import fileinput
import string
from collections import Counter
from functools import reduce
from operator import and_
from typing import List

# --- Day 4: Camp Cleanup ---
# --- Part one ---

sample_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".split(
    "\n"
)


def check_contain(first_pair: str, second_pair: str) -> int:
    first_pair = [int(_) for _ in first_pair.split("-")]
    second_pair = [int(_) for _ in second_pair.split("-")]

    if (second_pair[0] >= first_pair[0] and second_pair[1] <= first_pair[1]) or (
        first_pair[0] >= second_pair[0] and first_pair[1] <= second_pair[1]
    ):
        return 1

    return 0


def calc_sum_fully_contain(dat: List[str]):
    return sum([check_contain(*_.split(",")) for _ in dat])


assert calc_sum_fully_contain(sample_input) == 2

puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = calc_sum_fully_contain(puzzle_input)

assert solution_part1 == 524
print(f"solution part1: {solution_part1}")


# --- Part two ---

#
# def split_lines(dat: List[str], chunk_size=3):
#     for i in range(0, len(dat), chunk_size):
#         yield dat[i : i + chunk_size]
#
#
# assert calc_priority_sum(split_lines(sample_input), mode="part2") == 70
#
# solution_part2 = calc_priority_sum(split_lines(puzzle_input), mode="part2")
# assert solution_part2 == 2668
# print(f"solution part2: {solution_part2}")
