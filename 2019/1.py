#     --- Day 1: The Tyranny of the Rocket Equation ---
#     https://adventofcode.com/2019/day/1

# --- Read in data from file ---
with open("input1.txt", 'r') as file:
    data = [int(line.strip()) for line in file.readlines()]

# --- Part 1 ---    
def part_one(data) -> int:   
    total = 0

    for capsule in data:
        total += int(capsule / 3) - 2

    return total

# --- Part 2 ---
def part_two(data) -> int:
    total = 0
    
    for capsule in data:
        fuel = capsule
        while fuel > 2:
            fuel = int(fuel / 3) - 2
            total += fuel
    return total

# --- Answer ---
print(f"Part 1: {part_one(data)}")
print(f"Part 2: {part_two(data)}")