import fileinput
from dataclasses import dataclass
from typing import List

# --- Day 14: Regolith Reservoir ---
# --- Part one ---

sample_input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".split(
    "\n"
)

ROCK = "#"
AIR = "."
SAND = "+"


@dataclass(unsafe_hash=True)
class Coordinate:
    x: int
    y: int

    def update(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)


SAND_COORDINATE = Coordinate(500, 0)
DOWN_DELTA = Coordinate(0, 1)
DOWN_LEFT_DELTA = Coordinate(-1, 1)
DOWN_RIGHT_DELTA = Coordinate(1, 1)
DELTAS = [DOWN_DELTA, DOWN_LEFT_DELTA, DOWN_RIGHT_DELTA]


class Sand:
    def __init__(self, dat: List[str]):
        self.paths = Sand.fill(dat)
        self.bottom = None

    def simulate(self, mode="part1"):
        cave = self.fill_cave()
        if mode == "part1":
            return self.simulate_part1(cave)
        else:
            return self.simulate_part2(cave)

    def simulate_part1(self, cave):
        self.bottom = max([_.y for _ in cave])
        while True:
            actual_coordinate = SAND_COORDINATE
            is_rest = False
            while not is_rest:
                if actual_coordinate.y > self.bottom:
                    return len([_ for _ in cave.values() if _ == SAND])
                for delta in DELTAS:
                    if (next_coordinate := actual_coordinate.update(delta)) not in cave:
                        actual_coordinate = next_coordinate
                        break
                else:
                    is_rest = True
                    cave[actual_coordinate] = SAND

    def simulate_part2(self, cave):
        self.bottom = max([_.y for _ in cave]) + 1
        cave[SAND_COORDINATE] = SAND
        actual_coordinate = SAND_COORDINATE
        while True:
            if actual_coordinate in cave:  # restart at origin
                actual_coordinate = SAND_COORDINATE
            for delta in DELTAS:
                if (
                    next_coordinate := actual_coordinate.update(delta)
                ) not in cave and actual_coordinate.y < self.bottom:
                    actual_coordinate = next_coordinate
                    break
            else:
                cave[actual_coordinate] = SAND
            if actual_coordinate == SAND_COORDINATE:
                break
        return len([_ for _ in cave.values() if _ == SAND])

    def fill_cave(self):
        cave = {}

        for path in self.paths:
            for c1, c2 in zip(path, path[1:]):
                if c1.x == c2.x:
                    for y in range(min(c1.y, c2.y), max(c1.y, c2.y) + 1):
                        cave[Coordinate(c1.x, y)] = ROCK
                elif c1.y == c2.y:
                    for x in range(min(c1.x, c2.x), max(c1.x, c2.x) + 1):
                        cave[Coordinate(x, c1.y)] = ROCK
        return cave

    @staticmethod
    def fill(dat: List[str]):
        result = []
        for line in dat:
            coordinates = [Coordinate(*tuple(map(int, _.split(",")))) for _ in line.split(" -> ")]
            result.append(coordinates)
        return result


assert Sand(sample_input).simulate() == 24

puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = Sand(puzzle_input).simulate()

assert solution_part1 == 1513
print(f"solution part1: {solution_part1}")

# --- Part two ---

assert Sand(sample_input).simulate(mode="part2") == 93

solution_part2 = Sand(puzzle_input).simulate(mode="part2")
assert solution_part2 == 22646
print(f"solution part2: {solution_part2}")
