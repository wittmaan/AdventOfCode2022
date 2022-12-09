import fileinput
from dataclasses import dataclass
from typing import List

# --- Day 9: Rope Bridge ---
# --- Part one ---

sample_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".split(
    "\n"
)


@dataclass
class Instruction:
    direction: str
    steps: int

    def __post_init__(self):
        self.steps = int(self.steps)


@dataclass(unsafe_hash=True)
class Position:
    x: int
    y: int

    def move_needed(self, other: "Position", threshold=1):
        return abs(other.x - self.x) > threshold or abs(other.y - self.y) > threshold


class Rope:
    def __init__(self, dat: List[str], mode="part1"):
        self.moves = [Instruction(*_.split()) for _ in dat]
        self.visited = set()
        self.mode = mode

    def simulate(self):
        head = Position(0, 0)
        tail = Position(0, 0)
        knots = [Position(0, 0) for _ in range(10)] if self.mode == "part2" else None
        self.visited.add(Position(0, 0))

        for move in self.moves:
            for i in range(move.steps):
                if self.mode == "part1":
                    self.single_mode(head, move, tail)
                else:
                    self.multi_mode(knots, move)

        return len(self.visited)

    def single_mode(self, head, move, tail):
        if move.direction == "L":
            head.x -= 1
        elif move.direction == "R":
            head.x += 1
        elif move.direction == "U":
            head.y += 1
        elif move.direction == "D":
            head.y -= 1
        else:
            raise ValueError(f"unknown direction {move.direction}")
        self.update_single(head, tail)

    def update_single(self, head, tail, update_visits=True):
        if head.move_needed(tail):
            if head.x > tail.x:
                tail.x += 1
            elif head.x < tail.x:
                tail.x -= 1
            if head.y > tail.y:
                tail.y += 1
            elif head.y < tail.y:
                tail.y -= 1
            if update_visits:
                self.visited.add(Position(tail.x, tail.y))

    def multi_mode(self, knots, move):
        if move.direction == "L":
            knots[0].x -= 1
        elif move.direction == "R":
            knots[0].x += 1
        elif move.direction == "U":
            knots[0].y += 1
        elif move.direction == "D":
            knots[0].y -= 1
        else:
            raise ValueError(f"unknown direction {move.direction}")
        self.update_multi(knots)

    def update_multi(self, knots):
        for i in range(1, len(knots)):
            actual_position = knots[i - 1]
            previous_position = knots[i]
            self.update_single(actual_position, previous_position, update_visits=i == 9)


assert Rope(sample_input).simulate() == 13

puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = Rope(puzzle_input).simulate()

assert solution_part1 == 5513
print(f"solution part1: {solution_part1}")


# --- Part two ---

assert Rope(sample_input, mode="part2").simulate() == 1

sample_input2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".split(
    "\n"
)

assert Rope(sample_input2, mode="part2").simulate() == 36

solution_part2 = Rope(puzzle_input, mode="part2").simulate()
assert solution_part2 == 2427
print(f"solution part2: {solution_part2}")
