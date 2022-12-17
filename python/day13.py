import fileinput
from functools import cmp_to_key
from typing import List

# --- Day 13: Distress Signal ---
# --- Part one ---

sample_input = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


class DistressSignal:
    def __init__(self, dat: List[str], mode="part1"):
        self.packets = DistressSignal.fill(dat, mode)
        self.mode = mode

    @staticmethod
    def fill(dat: List[str], mode="part1"):
        packets = []
        for packet in dat:
            if mode == "part1":
                left, right = packet.split("\n")
                packets.append((eval(left), eval(right)))
            else:
                if packet == "":
                    continue
                packets.append(eval(packet))

        if mode == "part2":
            packets.append([[2]])
            packets.append([[6]])

        return packets

    def compare(self):
        if self.mode == "part1":
            num_correct_order = 0
            for idx, packet in enumerate(self.packets):
                if DistressSignal.compare_one_packet(left=packet[0], right=packet[1]):
                    num_correct_order += idx + 1
            return num_correct_order
        else:
            sorted_packets = sorted(
                self.packets,
                key=cmp_to_key(
                    lambda left, right: -1
                    if DistressSignal.compare_one_packet(left, right)
                    else 1
                ),
            )
            return (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)

    @staticmethod
    def compare_one_packet(left, right):
        for idx in range(max(len(left), len(right))):
            if idx == len(left) and idx < len(right):
                return 1
            if idx < len(left) and idx == len(right):
                return 0
            if isinstance(left[idx], int) and isinstance(right[idx], int):
                if left[idx] < right[idx]:
                    return 1
                if left[idx] > right[idx]:
                    return 0
            elif isinstance(left[idx], list) and isinstance(right[idx], list):
                result = DistressSignal.compare_one_packet(left[idx], right[idx])
                if result is not None:
                    return result
            elif isinstance(left[idx], int) and isinstance(right[idx], list):
                result = DistressSignal.compare_one_packet([left[idx]], right[idx])
                if result is not None:
                    return result
            elif isinstance(left[idx], list) and isinstance(right[idx], int):
                result = DistressSignal.compare_one_packet(left[idx], [right[idx]])
                if result is not None:
                    return result
        return None


assert DistressSignal(sample_input.split("\n\n")).compare() == 13

assert DistressSignal.compare_one_packet([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]) == 1
assert DistressSignal.compare_one_packet([[1], [2, 3, 4]], [[1], 4]) == 1


puzzle_input = "".join([_ for _ in fileinput.input()])
solution_part1 = DistressSignal(puzzle_input.split("\n\n")).compare()

assert solution_part1 == 5580
print(f"solution part1: {solution_part1}")

# --- Part two ---

assert DistressSignal(sample_input.split("\n"), mode="part2").compare() == 140

solution_part2 = DistressSignal(puzzle_input.split("\n"), mode="part2").compare()

assert solution_part2 == 26200
print(f"solution part2: {solution_part2}")
