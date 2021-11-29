#     --- Day 3: Perfectly Spherical Houses in a Vacuum ---
#     https://adventofcode.com/2015/day/3

from typing import Dict, Tuple

class House:
    def __init__(self, exists):
        self.exists = exists

    def __str__(self) -> str:
        return f"{self.exists}"

# Read in the data
file = open("input3.txt", 'r')
input = file.read()

# --- Part 1 ---
def part_1(input) -> int:
    position = [0, 0]
    houses: Dict[Tuple[int, int], House] = dict()
    houses[0, 0] = House(True)

    for order in input:
        if order == '^':
            position[1] += 1
        elif order == 'v':
            position[1] -= 1
        elif order == '>':
            position[0] += 1
        elif order == '<':
            position[0] -= 1
        else:
            raise RuntimeError(f"Got unexpected token")
        
        # If new position, create new House
        new_position = (position[0], position[1])
        if new_position not in houses:
            houses[new_position] = House(True)

    # Count Houses
    return len(houses.keys())

# --- Part 2 ---
def part_2(input) -> int:
    turn = 0
    santa = [0, 0]
    robo = [0, 0]
    houses: Dict[Tuple[int, int], House] = dict()
    houses[0, 0] = House(True)

    for order in input:
        turn += 1
        if order == '^':
            if turn % 2 == 1:
                santa[1] += 1
            else:
                robo[1] += 1
        elif order == 'v':
            if turn % 2 == 1:
                santa[1] -= 1
            else:
                robo[1] -= 1
        elif order == '>':
            if turn % 2 == 1:
                santa[0] += 1
            else:
                robo[0] += 1
        elif order == '<':
            if turn % 2 == 1:
                santa[0] -= 1
            else:
                robo[0] -= 1
        else:
            raise RuntimeError(f"Got unexpected token")
    
        # If new position, create new House
        if turn % 2 == 1:
            new_santa = (santa[0], santa[1])
            if new_santa not in houses:
                houses[new_santa] = House(True)
        else:
            new_robo = (robo[0], robo[1])
            if new_robo not in houses:
                houses[new_robo] = House(True)
    
    # Count Houses
    return len(houses.keys())

# Test Part 1
assert part_1(">") == 2
assert part_1("^>v<") == 4
assert part_1("^v^v^v^v^v") == 2

# Test Part 2
assert part_2("^v") == 3
assert part_2("^>v<") == 3
assert part_2("^v^v^v^v^v") == 11

# Answer
print(f"Part 1: {part_1(input)}")
print(f"Part 2: {part_2(input)}")
