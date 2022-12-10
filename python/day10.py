import fileinput
from dataclasses import dataclass
from typing import List, Optional

# --- Day 9: Rope Bridge ---
# --- Part one ---

sample_input1 = """noop
addx 3
addx -5""".split(
    "\n"
)

sample_input2 = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""".split(
    "\n"
)


@dataclass
class Instruction:
    type: str
    amount: Optional[int] = None

    def __post_init__(self):
        if self.amount is not None:
            self.amount = int(self.amount)


LIT_PIXEL = "#"
DARK_PIXEL = "."


class CathodeRayTube:
    def __init__(self, dat: List[str]):
        self.instructions = [Instruction(*_.split()) for _ in dat]
        self.height = 6
        self.width = 40
        self.pixels = [DARK_PIXEL] * self.width * self.height

    def execute(self, should_render=False) -> int:
        X = 1
        cycle = 0
        signal_strength = 0
        for instruction in self.instructions:
            self.update_pixels(X, cycle)
            cycle += 1
            if CathodeRayTube.update_signal_strength_needed(cycle):
                signal_strength += cycle * X

            if instruction.type == "addx":
                self.update_pixels(X, cycle)
                cycle += 1
                if CathodeRayTube.update_signal_strength_needed(cycle):
                    signal_strength += cycle * X

                X += instruction.amount

        if should_render:
            self.render()

        return signal_strength

    def render(self):
        for _ in range(self.height):
            print("".join(self.pixels[_ * self.width : (_ + 1) * self.width]))

    def update_pixels(self, X, cycle):
        if X - 1 <= cycle % 40 <= X + 1:
            self.pixels[cycle] = LIT_PIXEL

    @staticmethod
    def update_signal_strength_needed(cycle: int):
        return (cycle - 20) % 40 == 0


assert CathodeRayTube(sample_input1).execute() == 0
assert CathodeRayTube(sample_input2).execute() == 13140

puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = CathodeRayTube(puzzle_input).execute()

assert solution_part1 == 12520
print(f"solution part1: {solution_part1}")


# --- Part two ---

CathodeRayTube(puzzle_input).execute(should_render=True)
# EHPZPJGL
