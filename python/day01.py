import fileinput
from typing import List

# --- Day 1: Calorie Counting ---
# --- Part one ---

sample_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000""".split(
    "\n\n"
)


def get_top_most_calories(dat: List[List[str]], number=1) -> int:
    calories_per_elf = []
    for val in dat:
        calories_per_elf.append(sum([int(_) for _ in val.split("\n")]))
    return sum(sorted(calories_per_elf, reverse=True)[:number])


assert get_top_most_calories(sample_input) == 24000

puzzle_input = ("".join([_ for _ in fileinput.input()])).split("\n\n")
solution_part1 = get_top_most_calories(puzzle_input)

assert solution_part1 == 72478
print(f"solution part1: {solution_part1}")


# --- Part two ---

assert get_top_most_calories(sample_input, number=3) == 45000
solution_part2 = get_top_most_calories(puzzle_input, number=3)
assert solution_part2 == 210367
print(f"solution part2: {solution_part2}")
