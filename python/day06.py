import fileinput

# --- Day 6: Tuning Trouble ---
# --- Part one ---

sample_input1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
sample_input2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
sample_input3 = "nppdvjthqldpwncqszvftbrmjlhg"
sample_input4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
sample_input5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"


def detect_marker(dat: str, limit=4):
    for i in range(limit, len(dat)):
        packet = dat[i - limit : i]
        if len(set(packet)) == limit:
            return i


assert detect_marker(sample_input1) == 7
assert detect_marker(sample_input2) == 5
assert detect_marker(sample_input3) == 6
assert detect_marker(sample_input4) == 10
assert detect_marker(sample_input5) == 11

puzzle_input = [_ for _ in fileinput.input()][0]

solution_part1 = detect_marker(puzzle_input)

assert solution_part1 == 1343
print(f"solution part1: {solution_part1}")

# --- Part two ---

solution_part2 = detect_marker(puzzle_input, limit=14)

assert solution_part1 == 2193
print(f"solution part1: {solution_part2}")
