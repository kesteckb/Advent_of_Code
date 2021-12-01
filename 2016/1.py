#     --- Day 1: Corruption Checksum ---
#     https://adventofcode.com/2016/day/1

import enum

# Read in the data
file = open("input1.txt", 'r')
data = file.readline()
instructions = [command.strip() for command in data.split(',')]

class Directions(enum.Enum):
    North = 0
    East = 1
    South = 2
    West = 3

# --- Part 1 ---
def part_1(instructions) -> int:
    # Start position
    path = Directions.North
    x = 0 
    y = 0

    for instruction in instructions:    
        # Handle direction
        if instruction[0] == "R":
            if path == Directions.West:
                path = Directions.North
            elif path == Directions.North:
                path = Directions.East
            elif path == Directions.East:
                path = Directions.South 
            elif path == Directions.South:
                path = Directions.West        
        elif instruction[0] == "L":
            if path == Directions.West:
                path = Directions.South
            elif path == Directions.North:
                path = Directions.West
            elif path == Directions.East:
                path = Directions.North 
            elif path == Directions.South:
                path = Directions.East        
        else:
            raise RuntimeError(f"Got unexpected token")
        
        # Handle Distance
        if path == Directions.North:
            y += int(instruction[1:])
        elif path == Directions.South:
            y -= int(instruction[1:])
        elif path == Directions.East:
            x += int(instruction[1:])
        elif path == Directions.West:
            x -= int(instruction[1:])
        else:
            raise RuntimeError(f"Got unexpected token")

    return abs(x) + abs(y)

# --- Test Part 1 ---
assert part_1(['R2', 'L3']) == 5
assert part_1(['R2', 'R2', 'R2']) == 2
assert part_1(['R5', 'L5', 'R5', 'R3']) == 12

# Answer
print(f"Part 1: {part_1(instructions)}")