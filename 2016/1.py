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

# --- Part 2 ---
def part_2(instructions) -> int:
    visited = ([0, 0])
    x = 0
    y = 0
    path = Directions.North

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
        distance = int(instruction[1:])
        if path == Directions.North:
            for idx in range(distance):
                y += 1
                if [x, y] in visited:
                    return abs(x) + abs(y)
                else:
                    visited.append([x, y])
        elif path == Directions.South:
            for idx in range(distance):
                y -= 1
                if [x, y] in visited:
                    return abs(x) + abs(y)
                else:
                    visited.append([x, y])            
        elif path == Directions.East:
            for idx in range(distance):
                x += 1
                if [x, y] in visited:
                    return abs(x) + abs(y)
                else:
                    visited.append([x, y])            
        elif path == Directions.West:
            for idx in range(distance):
                x -= 1
                if [x, y] in visited:
                    return abs(x) + abs(y)
                else:
                    visited.append([x, y])            
        else:
            raise RuntimeError(f"Got unexpected token")


    return distance

# --- Test Part 1 ---
assert part_1(['R2', 'L3']) == 5
assert part_1(['R2', 'R2', 'R2']) == 2
assert part_1(['R5', 'L5', 'R5', 'R3']) == 12

# --- Test Part 2 ---
assert part_2(['R8', 'R4', 'R4', 'R8']) == 4

# Answer
print(f"Part 1: {part_1(instructions)}")
print(f"Part 2: {part_2(instructions)}")

# Close file
file.close()