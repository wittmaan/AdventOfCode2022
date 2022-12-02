import fileinput
from typing import List

# --- Day 1: Calorie Counting ---
# --- Part one ---

sample_input = """A Y
B X
C Z""".split(
    "\n"
)

ROCK = "ROCK"
PAPER = "PAPER"
SCISSORS = "Scissors"

STRATEGY_GUIDE = {ROCK: 1, PAPER: 2, SCISSORS: 3}
OTHER_MAPPING = {"A": ROCK, "B": PAPER, "C": SCISSORS}
OWN_MAPPING = {"X": ROCK, "Y": PAPER, "Z": SCISSORS}


def play(dat: List[str]) -> int:
    other_val = STRATEGY_GUIDE[OTHER_MAPPING[dat[0]]]
    own_val = STRATEGY_GUIDE[OWN_MAPPING[dat[1]]]

    difference = (other_val - own_val) % 3
    if difference == 2:
        return own_val + 6
    elif difference == 0:
        return own_val + 3
    elif difference == 1:
        return own_val + 0


def calc_total_score(dat: List[str]) -> int:
    return sum([play(_.split()) for _ in dat])


assert calc_total_score(sample_input) == 15

puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = calc_total_score(puzzle_input)

assert solution_part1 == 14827
print(f"solution part1: {solution_part1}")


# --- Part two ---


# assert solution_part2 == 210367
# print(f"solution part2: {solution_part2}")
