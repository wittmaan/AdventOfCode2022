import fileinput
from dataclasses import dataclass
from re import findall
from typing import List

from tqdm import tqdm

# --- Day 15: Beacon Exclusion Zone ---
# --- Part one ---


sample_input = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".split(
    "\n"
)


@dataclass(unsafe_hash=True)
class Position:
    x: int
    y: int

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


class Sensor:
    def __init__(self, dat):
        self.position = Position(dat[0], dat[1])
        self.beacon = Position(dat[2], dat[3])
        self.distance_to_beacon = self.distance(self.beacon)

    def distance(self, other):
        return self.position.distance(other)


class ExclusionZone:
    def __init__(self, dat: List[str]):
        self.sensors = [ExclusionZone.parse(_) for _ in dat]
        self.beacons = None

    def filter(self, y=10):
        result = []
        for sensor in self.sensors:
            if sensor.distance(Position(sensor.position.x, y)) <= sensor.distance_to_beacon:
                result.append(sensor)
        return result

    def is_beacon_possible(self, position: Position):
        for sensor in self.sensors:
            if sensor.position.distance(position) <= sensor.distance_to_beacon and position not in self.beacons:
                return False
        return True

    def count_positions_not_containing_beacon(self, y=10):
        self.sensors = self.filter(y)
        self.beacons = set([_.beacon for _ in self.sensors])
        min_x_distance = min([sensor.position.x - sensor.distance_to_beacon for sensor in self.sensors])
        max_x_distance = max([sensor.position.x + sensor.distance_to_beacon for sensor in self.sensors])
        count = 0
        for x in tqdm(range(min_x_distance, max_x_distance)):
            if not self.is_beacon_possible(Position(x, y)):
                count += 1
        return count

    def calc_tuning_frequency(self, limits=(0, 4000000)):
        self.beacons = set([_.beacon for _ in self.sensors])
        for sensor in tqdm(self.sensors):
            for delta_x in tqdm(range(sensor.distance_to_beacon + 2)):
                delta_y = (sensor.distance_to_beacon + 1) - delta_x
                for dx, dy in [(-1, 1), (1, -1), (-1, -1), (1, 1)]:
                    x, y = sensor.position.x + (delta_x * dx), sensor.position.y + (delta_y * dy)
                    if not (limits[0] <= x <= limits[1] and limits[0] <= y <= limits[1]):
                        continue
                    if self.is_beacon_possible(Position(x, y)):
                        return x * limits[1] + y

    @staticmethod
    def parse(dat: str) -> Sensor:
        return Sensor([int(_) for _ in findall(r"(-?\d+)", dat)])


assert ExclusionZone(sample_input).count_positions_not_containing_beacon() == 26

puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = ExclusionZone(puzzle_input).count_positions_not_containing_beacon(y=2000000)

assert solution_part1 == 4737443
print(f"solution part1: {solution_part1}")

# --- Part two ---

solution_part2 = ExclusionZone(puzzle_input).calc_tuning_frequency()

assert solution_part2 == 11482462818989
print(f"solution part2: {solution_part2}")
