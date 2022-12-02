import fileinput
from typing import List

# --- Day 1: Calorie Counting ---
# --- Part one ---

sample_input = """A Y
B X
C Z""".split(
    "\n"
)

LOSE = 0
DRAW = 3
WIN = 6

ROCK = "ROCK"
PAPER = "PAPER"
SCISSORS = "Scissors"

STRATEGY_GUIDE = {ROCK: 1, PAPER: 2, SCISSORS: 3}
OTHER_MAPPING = {"A": ROCK, "B": PAPER, "C": SCISSORS}
OWN_MAPPING = {"X": ROCK, "Y": PAPER, "Z": SCISSORS}


def play(dat: List[str], mode="part1") -> int:
    other_val = STRATEGY_GUIDE[OTHER_MAPPING[dat[0]]]
    own_val = STRATEGY_GUIDE[OWN_MAPPING[dat[1]]]

    if mode == "part1":
        difference = (other_val - own_val) % 3
        if difference == 0:
            return own_val + DRAW
        elif difference == 1:
            return own_val + LOSE
        elif difference == 2:
            return own_val + WIN
    else:
        if own_val == 2:
            return other_val + DRAW
        elif own_val == 1:
            return (other_val - 2) % 3 + 1 + LOSE
        elif own_val == 3:
            return other_val % 3 + 1 + WIN


def calc_total_score(dat: List[str], mode="part1") -> int:
    return sum([play(_.split(), mode) for _ in dat])


assert calc_total_score(sample_input) == 15

puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = calc_total_score(puzzle_input)

assert solution_part1 == 14827
print(f"solution part1: {solution_part1}")


# --- Part two ---

assert calc_total_score(sample_input, mode="part2") == 12
solution_part2 = calc_total_score(puzzle_input, mode="part2")

assert solution_part2 == 13889
print(f"solution part2: {solution_part2}")
