#     --- Day 7: The Treachery of Whales ---
#     https://adventofcode.com/2021/day/7

import statistics

with open("input7.txt", 'r') as file:
    data = [int(x) for x in file.readline().split(',')]

example = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

def part_one(data) -> int:
    crab_army = data
    fuel = 0
    location = int(statistics.median(crab_army))
    for crab in crab_army:
        fuel += abs(crab - location)

    return fuel

def part_two(data) -> int:
    crab_army = data
    fuel = 0
    location = round(statistics.mean(crab_army))
    for crab in crab_army:
        fuel += get_fuel(abs(crab - location))

    return fuel

def get_fuel(difference) -> int:
    # 5+4+3+2+1 = 15
    total = 0   
    for x in range(difference, 0, -1):
        total += x
    return total

# --- Answer ---
print(f"Part 1: {part_one(data)}")
print(f"Part 2: {part_two(data)}")
