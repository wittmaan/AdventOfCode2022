import fileinput
from typing import List

# --- Day 8: Treetop Tree House ---
# --- Part one ---

sample_input = """30373
25512
65332
33549
35390""".split(
    "\n"
)


class Grid:
    def __init__(self, dat: List[str]):
        self.grid = dat
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def find_visible_trees(self) -> int:
        # visible at the edge
        visible = self.height * 2 + self.width * 2 - 4
        for idx_row, row in enumerate(self.grid):
            # skip edge
            if idx_row == 0 or idx_row == self.height - 1:
                continue

            for idx_col, tree in enumerate(row):
                # skip edge
                if idx_col == 0 or idx_col == self.width - 1:
                    continue

                if Grid.check_row(idx_col, row, tree) or self.check_column(idx_col, idx_row, tree):
                    visible += 1

        return visible

    def check_column(self, idx_col, idx_row, tree) -> bool:
        top = [tree > self.grid[i][idx_col] for i in range(idx_row + 1, len(self.grid))]
        bottom = [tree > self.grid[i][idx_col] for i in range(idx_row - 1, -1, -1)]
        return all(bottom) or all(top)

    @staticmethod
    def check_row(idx_col, row, tree) -> bool:
        left = [tree > t for t in row[idx_col + 1 :]]
        right = [tree > t for t in row[:idx_col]]
        return all(left) or all(right)

    def find_highest_scenic_score(self) -> int:
        score = 0
        for idx_row, row in enumerate(self.grid):
            # skip edge
            if idx_row == 0 or idx_row == self.height - 1:
                continue

            for idx_col, tree in enumerate(row):
                # skip edge
                if idx_col == 0 or idx_col == self.width - 1:
                    continue

                for left in range(idx_col + 1, self.width):
                    if row[left] >= tree:
                        break

                for right in range(idx_col - 1, -1, -1):
                    if row[right] >= tree:
                        break

                for top in range(idx_row + 1, self.height):
                    if self.grid[top][idx_col] >= tree:
                        break

                for bottom in range(idx_row - 1, -1, -1):
                    if self.grid[bottom][idx_col] >= tree:
                        break

                actual_value = (left - idx_col) * (idx_col - right) * (top - idx_row) * (idx_row - bottom)
                score = max(score, actual_value)

        return score


assert Grid(sample_input).find_visible_trees() == 21

puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = Grid(puzzle_input).find_visible_trees()

assert solution_part1 == 1711
print(f"solution part1: {solution_part1}")


# --- Part two ---

assert Grid(sample_input).find_highest_scenic_score() == 8

solution_part2 = Grid(puzzle_input).find_highest_scenic_score()
assert solution_part2 == 301392
print(f"solution part2: {solution_part2}")
