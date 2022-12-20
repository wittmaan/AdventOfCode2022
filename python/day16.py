
# --- Day 16: Proboscidea Volcanium ---
# --- Part one ---
from typing import List, Set

sample_input = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".split("\n")

class ProboscideaVolcanium:
    def __init__(self, dat: List[str]):
        pass

    def solve(self):
        opened = set()
        ProboscideaVolcanium.dfs("AA", 0, 0, opened)

    @staticmethod
    def dfs(current_valve: str, actual_time: int, total_time: int, opened: Set[str]):
        # remaining time = 30 - actual_time
        maximum_flow = total_time # + flow from all opened vales * remaining time

        # try to open more valves
        # go through all valves that have non-zero troughput




# graph = {
#     'A' : ['B','C'],
#     'B' : ['D', 'E'],
#     'C' : ['F'],
#     'D' : [],
#     'E' : ['F'],
#     'F' : []
# }
#
# visited = set() # Set to keep track of visited nodes.
#
# def dfs(visited, graph, node):
#     if node not in visited:
#         print (node)
#         visited.add(node)
#         for neighbour in graph[node]:
#             dfs(visited, graph, neighbour)
#
# # Driver Code
# dfs(visited, graph, 'A')


# --- Part two ---