#     --- Day 1: Sonar Sweep ---
#     https://adventofcode.com/2021/day/1

# Read data from file
with open("input1.txt", 'r') as file:
    data = file.readlines()
    data = [int(line) for line in data]

# --- Part 1 ---
def part_1(data) -> int:
    depth_increases = 0

    for idx, depth in enumerate(data):
        if idx > 0:
            previous = data[idx-1]
            if depth > previous:
                depth_increases += 1
            previous = depth

    return depth_increases

# --- Part 2 ---
def part_2(data) -> int:
    depth_increases = 0

    for idx, depth in enumerate(data):
        if idx > 2:
            previous = data[idx-3] + data[idx-2] + data[idx-1]
            if (depth + data[idx -1] + data[idx-2] > previous):
                depth_increases += 1
    
    return depth_increases

# --- Test Part 1 ---
assert part_1([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 7

# --- Answer ---
print(f"Part 1: {part_1(data)}")
print(f"Part 2: {part_2(data)}")

# Close file
file.close()