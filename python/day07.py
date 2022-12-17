import fileinput
from dataclasses import dataclass
from typing import Set, List

# --- Day 7: No Space Left On Device ---
# --- Part one ---

sample_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".split(
    "\n"
)


@dataclass(unsafe_hash=True)
class File:
    name: str
    size: int


class Directory:
    def __init__(self, name: str, parent: "Directory" = None):
        self.name = name
        self.parent = parent
        self.files: Set[File] = set()
        self.directories: Set[Directory] = set()

    def cd(self, name: str):
        return [_ for _ in self.directories if _.name == name][0]

    def size(self):
        return sum([file.size for file in self.files]) + sum([directory.size() for directory in self.directories])


class Terminal:
    def __init__(self):
        self.root = Directory("/")
        self.current_working_directory: Directory = self.root

    def cd(self, name: str):
        if name == "/":
            self.current_working_directory = self.root
        elif name == "..":
            if self.current_working_directory.parent is not None:
                self.current_working_directory = self.current_working_directory.parent
        else:
            self.current_working_directory = self.current_working_directory.cd(name)

    def fill(self, command: str):
        if command.startswith("dir"):
            self.current_working_directory.directories.add(
                Directory(name=command.split()[-1], parent=self.current_working_directory)
            )
        else:
            file_size, file_name = command.split()
            self.current_working_directory.files.add(File(name=file_name, size=int(file_size)))

    def run_commands(self, commands: List[str]):
        for command in commands:
            if command.startswith("$ ls"):
                continue
            elif command.startswith("$ cd"):
                self.cd(name=command.split()[-1])
            else:
                self.fill(command)

    def find(self, directory: Directory, threshold, mode="part1"):
        if mode == "part1":
            directories = [directory] if directory.size() <= threshold else []
        else:
            directories = [directory] if directory.size() >= threshold else []

        for subdirectory in directory.directories:
            directories += self.find(subdirectory, threshold, mode)

        return directories

    def calc_total_sizes(self, threshold=100000):
        total_size = 0
        for directory in self.find(self.root, threshold):
            actual_size = directory.size()
            if actual_size is not None:
                total_size += actual_size
        return total_size

    def find_smallest_directory(self):
        space_needed = 30000000
        space_available = 70000000 - self.root.size()
        return min([_.size() for _ in self.find(self.root, space_needed - space_available, mode="part2")])


def calc_total_sizes_directories(dat: List[str]) -> int:
    terminal = Terminal()
    terminal.run_commands(dat)
    return terminal.calc_total_sizes()


assert calc_total_sizes_directories(sample_input) == 95437

puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = calc_total_sizes_directories(puzzle_input)

assert solution_part1 == 1243729
print(f"solution part1: {solution_part1}")

# --- Part two ---


def find_smallest_directory(dat: List[str]) -> int:
    terminal = Terminal()
    terminal.run_commands(dat)
    return terminal.find_smallest_directory()


assert find_smallest_directory(sample_input) == 24933642


solution_part2 = find_smallest_directory(puzzle_input)

assert solution_part2 == 4443914
print(f"solution part2: {solution_part2}")
