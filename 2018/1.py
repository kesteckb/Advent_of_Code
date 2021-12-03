#     --- Day 1: Chronal Calibration ---
#     https://adventofcode.com/2018/day/1

with open("input1.txt", 'r') as file:
    data = [int(x.replace('+', '')) for x in file]

# --- Part 2 ---
def part_2(data) -> int:
    frequency = 0
    seen = {frequency}
    loop = True
    
    while loop == True:
        for x in data:
            frequency += x
            if frequency in seen:
                return frequency
            else:
                seen.add(frequency)

# --- Answer ---
print(f"Part 1: {sum(data)}")
print(f"Part 2: {part_2(data)}")