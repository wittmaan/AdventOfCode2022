import fileinput
from typing import List, Tuple

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


def get_most_calories(dat: List[List[str]]) -> Tuple[int, int]:
    most_calories = None
    idx_most_calories = None
    for idx, val in enumerate(dat):
        result = val.split("\n")
        result = sum([int(_) for _ in result])

        if most_calories is None or result > most_calories:
            most_calories = result
            idx_most_calories = idx
    return most_calories, idx_most_calories


assert get_most_calories(sample_input) == (24000, 3)

puzzle_input = ("".join([_ for _ in fileinput.input()])).split("\n\n")
solution_part1 = get_most_calories(puzzle_input)

assert solution_part1 == (72478, 122)
print(f"solution part1: {solution_part1}")


# --- Part two ---


def get_top_most_calories(dat: List[List[str]], number=3) -> int:
    calories_per_elf = []
    for idx, val in enumerate(dat):
        result = val.split("\n")
        result = sum([int(_) for _ in result])
        calories_per_elf.append(result)

    return sum(sorted(calories_per_elf, reverse=True)[:number])


assert get_top_most_calories(sample_input) == 45000
solution_part2 = get_top_most_calories(puzzle_input)
assert solution_part2 == 210367
print(f"solution part2: {solution_part2}")
