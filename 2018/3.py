#     --- Day 3: No Matter How You Slice It ---
#     https://adventofcode.com/2018/day/3

import re

with open("input3.txt",'r') as file:
    data = [line.strip().split('\n') for line in file]

example1 = [
    ['#1 @ 1,3: 4x4'],
    ['#2 @ 3,1: 4x4'],
    ['#3 @ 5,5: 2x2'],
]

# --- Part 1 ---
def part_1(data) -> int:
    claimed = set()
    overlapped = set()

    for claim in data:
        id = claim[0]
        from_left = claim[1]
        from_top = claim[2]
        width = claim[3]
        height = claim[4]

        for idx in range(width):
            for jdx in range(height):
                coordinate = (from_left + idx, -(from_top + jdx))
                if coordinate in claimed:
                    overlapped.add(coordinate)
                else:
                    claimed.add(coordinate)
    return len(overlapped)

# --- Part 2 ---
def part_2(data) -> set:
    claimed = set()
    overlapped = set()
    

    for claim in data:
        id = claim[0]
        from_left = claim[1]
        from_top = claim[2]
        width = claim[3]
        height = claim[4]

        for idx in range(width):
            for jdx in range(height):
                coordinate = (from_left + idx, -(from_top + jdx))
                if coordinate in claimed:
                    overlapped.add(coordinate)
                else:
                    claimed.add(coordinate)
        
    return ids

def parse_input(data) -> list:
    new_list = []
    
    for line in data:
        for claim in line:
            new_list.append(re.findall(r'\d+', claim))
    new_list = [[int(x) for x in line] for line in new_list]

    return new_list

# --- Testing ---
assert part_1(parse_input(example1)) == 4


print(f"Part 1: {part_1(parse_input(data))}")
print(f"Part 2: {part_2(parse_input(data))}")