#     --- Day 3: No Matter How You Slice It ---
#     https://adventofcode.com/2018/day/3

from collections import Counter
import re

with open("input3.txt",'r') as file:
    data = [line.strip().split('\n') for line in file]

class Claim:
    def __init__(self, id, from_left, from_top, width, height):
        self.id = id
        self.from_left = from_left
        self.from_top = from_top
        self.width = width
        self.height = height
        self.coordinates = set()

    def __str__(self):
        return f'Claim({self.id},{self.from_left},{self.from_top},{self.width},{self.height})'

    def update_coordinates(self, coordinate):
        self.coordinates.add(coordinate)

    def get_coordinates(self):
        print(f"Coordinates in #{self.id}: {self.coordinates}")

    def all_good(self, key_list) -> bool:
        for coordinate in self.coordinates:
            if coordinate not in key_list:
                return False
        return True

    def is_in_claim(self, coordinate) -> bool:
        return coordinate in self.coordinates
    
    def get_id(self) -> int:
        return self.id

    def get_from_left(self) -> int:
        return self.from_left

    def get_from_top(self) -> int:
        return self.from_top

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

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
def part_2(data) -> int:
    claims = []
    all_coordinates = []

    # Create array list of Claims and update the coordinates they occupy
    for idx, claim in enumerate(data):
        claims.append(Claim(claim[0], claim[1], claim[2], claim[3], claim[4]))
        for hrz in range(claims[idx].get_width()):
            for vrt in range(claims[idx].get_height()):
                coordinate = (claims[idx].get_from_left() + hrz, -(claims[idx].get_from_top() + vrt))
                claims[idx].update_coordinates(coordinate)
                all_coordinates.append(coordinate)

    # Get occurance of coordinates (most - least) and set target equal to a
    # coordinate which occurs only once
    histogram = dict(Counter(all_coordinates).most_common(len(all_coordinates)))
    key_list = list(histogram.keys())
    val_list = list(histogram.values())

    # Lists only contain unique coordinates (keys)
    while val_list[0] > 1:
        del key_list[0]
        del val_list[0]

    # Here we go!!!
    for claim in claims:
        if claim.all_good(key_list):
            return claim.get_id()
        
def parse_input(data) -> list:
    new_list = []
    
    for line in data:
        for claim in line:
            new_list.append(re.findall(r'\d+', claim))
    new_list = [[int(x) for x in line] for line in new_list]

    return new_list

# --- Testing ---
assert part_1(parse_input(example1)) == 4
assert part_2(parse_input(example1)) == 3

print(f"Part 1: {part_1(parse_input(data))}")
print(f"Part 2: {part_2(parse_input(data))}")