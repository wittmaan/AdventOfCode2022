# --- Day 16: Proboscidea Volcanium ---
# --- Part one ---
from collections import deque
from contextlib import suppress
from dataclasses import dataclass
from functools import cached_property
from typing import List, Dict, FrozenSet

sample_input = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".split(
    "\n"
)


@dataclass(unsafe_hash=True)
class Valve:
    name: str
    rate: int
    valves: frozenset

    def __repr__(self) -> str:
        return f"{self.name} {self.rate} {self.valves}"


class Tunnel:
    def __init__(self, valve: Valve, time_left: int = 30, total_released: int = 0, opened: FrozenSet = frozenset()):
        self.valve = valve
        self.time_left = time_left
        self.total_released = total_released
        self.opened = opened

    def on_next_valve(self, distances: Dict[Valve, Dict[Valve, int]]):
        for other_valve, distance in distances[self.valve].items():
            if other_valve in self.opened or not other_valve.rate:
                continue
            if (time_left := self.time_left - (distance + 1)) <= 0:
                continue
            yield __class__(
                other_valve, time_left, self.total_released + other_valve.rate * time_left, self.opened | {other_valve}
            )


class ProboscideaVolcanium:
    def __init__(self, dat: List[str]):
        self.valves: Dict[str, Valve] = ProboscideaVolcanium.parse(dat)

    def solve(self) -> int:
        time_left = 30
        starting_valve = self.valves["AA"]
        max_released: Dict[FrozenSet[Valve], int] = {}
        stack = deque([Tunnel(starting_valve, time_left)])

        while stack:
            actual_tunnel = stack.popleft()
            for next_item in actual_tunnel.on_next_valve(self.distances):
                stack.append(next_item)
                max_released[next_item.opened] = max(max_released.get(next_item.opened, 0), next_item.total_released)

        return max(max_released.values())

    @staticmethod
    def parse(dat: List[str]):
        result = {}
        for line in dat:
            line_splitted = line.split(" ")
            valve_name = line_splitted[1]
            flow_rate = int(line_splitted[4].split("=")[1][:-1])
            valves = frozenset([_.replace(",", "") for _ in line_splitted[9:]])
            result[valve_name] = Valve(valve_name, flow_rate, valves)
        return result

    @cached_property
    def distances(self) -> Dict[Valve, Dict[Valve, int]]:
        dist: Dict[Valve, Dict[Valve, int]] = {}
        for valve in self.valves.values():
            dist[valve] = {self.valves[n]: 1 for n in valve.valves}

        len_valves = len(self.valves)
        for k in self.valves.values():
            for i in self.valves.values():
                for j in self.valves.values():
                    with suppress(KeyError):
                        dist[i][j] = min(dist[i].get(j, len_valves), dist[i][k] + dist[k][j])

        return dist


assert ProboscideaVolcanium(sample_input).solve() == 1651


# --- Part two ---
