#     --- Day 2: Dive! ---
#     https://adventofcode.com/2021/day/2

# --- Get input ---
with open("input2.txt", 'r') as file:
    lines = [[x for x in line.strip().split()] for line in file]

example = [
    ['forward', '5'],
    ['down', '5'],
    ['forward', '8'],
    ['up', '3'],
    ['down', '8'],
    ['forward', '2'],
]

# --- Part 1 ---
def part_1(lines) -> int:
    depth = 0
    forward = 0

    for line in lines:
        if line[0] == 'forward':
            forward += int(line[1])
        elif line[0] == 'up':
            depth -= int(line[1])
        elif line[0] == 'down':
            depth += int(line[1])
        else:
            raise RuntimeError(f"Got unexpected token")
    return depth * forward

# --- Part 2 ---
def part_2(lines) -> int:
    depth = 0
    forward = 0
    aim = 0

    for line in lines:
        if line[0] == 'forward':
            forward += int(line[1])
            depth += aim * int(line[1])
        elif line[0] == 'up':
            aim -= int(line[1])
        elif line[0] == 'down':
            aim += int(line[1])
        else:
            raise RuntimeError(f"Got unexpected token")
    return depth * forward

# --- Test ---
assert part_1(example) == 150
assert part_2(example) == 900

# --- Answer ---
print(f"Part 1: {part_1(lines)}")
print(f"Part 2: {part_2(lines)}")