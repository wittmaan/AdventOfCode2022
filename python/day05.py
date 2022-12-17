import fileinput
from collections import defaultdict, deque
from copy import deepcopy
from dataclasses import dataclass
from typing import List

# --- Day 5: Supply Stacks ---
# --- Part one ---

sample_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


@dataclass
class Instruction:
    index: int
    source: int
    target: int


def parse_input(dat: str):
    stacks = defaultdict(deque)
    for stack_entry in dat.split("\n\n")[0].split("\n")[:-1]:
        for ch in range(0, len(stack_entry), 4):
            if stack_entry[ch : ch + 4][0] == "[":
                stacks[ch // 4 + 1].append(stack_entry[ch : ch + 4][1])

    instructions: List[Instruction] = []
    for instruction_entry in dat.split("\n\n")[1].split("\n"):
        instructions.append(Instruction(*[int(_) for _ in instruction_entry.split(" ") if _.isnumeric()]))

    return stacks, instructions


def rearrange(dat: str, mode="part1"):
    stacks, instructions = parse_input(dat)
    stacks2 = deepcopy(stacks)

    for instruction in instructions:
        group_same_order = []
        for _ in range(instruction.index):
            stacks[instruction.target].appendleft(stacks[instruction.source].popleft())
            group_same_order.append(stacks2[instruction.source].popleft())
        stacks2[instruction.target].extendleft(group_same_order[::-1])

    if mode == "part1":
        return "".join([v[0] for _, v in sorted(stacks.items())])
    else:
        return "".join([v[0] for _, v in sorted(stacks2.items())])


assert rearrange(sample_input) == "CMZ"

puzzle_input = "".join([_ for _ in fileinput.input()])
solution_part1 = rearrange(puzzle_input)

assert solution_part1 == "ZRLJGSCTR"
print(f"solution part1: {solution_part1}")


# --- Part two ---

assert rearrange(sample_input, mode="part2") == "MCD"

solution_part2 = rearrange(puzzle_input, mode="part2")
assert solution_part2 == "PRTTGRFPB"
print(f"solution part2: {solution_part2}")
