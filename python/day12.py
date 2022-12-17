import fileinput
from collections import deque
from dataclasses import dataclass
from typing import List

# --- Day 12: Hill Climbing Algorithm ---
# --- Part one ---

sample_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".split(
    "\n"
)


@dataclass(unsafe_hash=True)
class Position:
    i: int
    j: int
    elevation: int

    def __eq__(self, other):
        return self.i == other.i and self.j == other.j


class HillClimbing:
    def __init__(self, dat: List[str]):
        self.grid, self.source, self.target = HillClimbing.fill(dat)
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.grid[self.source.i][self.source.j].elevation = 0
        self.grid[self.target.i][self.target.j].elevation = 25

    @staticmethod
    def fill(dat: List[str]):
        positions = []
        source = None
        target = None
        for idx1, row in enumerate(dat):
            positions_row = []
            for idx2, char in enumerate(row):
                positions_row.append(Position(i=idx1, j=idx2, elevation=ord(char) - ord("a")))
                if char == "S" and source is None:
                    source = Position(i=idx1, j=idx2, elevation=0)
                if char == "E" and target is None:
                    target = Position(i=idx1, j=idx2, elevation=0)
            positions.append(positions_row)

        return positions, source, target

    def find_path(self, mode="part1"):
        if mode == "part2":
            self.source, self.target = self.target, self.source
        actual_path = deque([(self.source, 0)])
        visited_positions = set()
        while actual_path:
            actual_position, steps = actual_path.popleft()
            # print(f"{actual_position} / {steps}")
            if mode == "part1" and actual_position == self.target:
                return steps
            elif mode == "part2" and actual_position != self.source and actual_position.elevation == 0:
                return steps
            if actual_position in visited_positions:
                continue
            visited_positions.add(actual_position)
            for neighbor in self.get_neighbors(actual_position, mode):
                actual_path.append((neighbor, steps + 1))
        return None

    def get_neighbors(self, position, mode="part1"):
        deltas = [
            (position.i + 1, position.j),
            (position.i - 1, position.j),
            (position.i, position.j - 1),
            (position.i, position.j + 1),
        ]
        result = []
        if mode == "part1":
            for delta in deltas:
                if delta[0] in range(self.height) and delta[1] in range(self.width):
                    delta_position = self.get_position(delta)
                    if delta_position is not None and (delta_position.elevation - position.elevation) <= 1:
                        result.append(delta_position)
        else:
            for delta in deltas:
                if delta[0] in range(self.height) and delta[1] in range(self.width):
                    delta_position = self.get_position(delta)
                    if delta_position is not None and (position.elevation - delta_position.elevation) <= 1:
                        result.append(delta_position)
        return result

    def get_position(self, delta):
        for row in self.grid:
            for position in row:
                if position.i == delta[0] and position.j == delta[1]:
                    return position
        return None


assert HillClimbing(sample_input).find_path() == 31

puzzle_input = ("".join([_ for _ in fileinput.input()])).split("\n")
solution_part1 = HillClimbing(puzzle_input).find_path()

assert solution_part1 == 504
print(f"solution part1: {solution_part1}")


# --- Part two ---

assert HillClimbing(sample_input).find_path(mode="part2") == 23

solution_part2 = HillClimbing(puzzle_input).find_path(mode="part2")
assert solution_part2 == 500
print(f"solution part2: {solution_part2}")
