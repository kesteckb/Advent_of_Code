#     --- Day 6: Lanternfish ---
#     https://adventofcode.com/2021/day/6

from collections import defaultdict

with open("input6.txt", 'r') as file:
    data = [int(x) for x in file.readline().split(',')]

example = [3, 4, 3, 1, 2]

def part_one(data):
    num_days = 80
    
    for _ in range(num_days):
        for idx, fish in enumerate(data):
            if fish == 0:
                data[idx] = 6
                data.append(9)
            else:
                data[idx] -= 1
    return len(data)

def part_two(data):
    num_days = 256
    fish_dict = defaultdict(int)

    # Initialize dictionary
    for num in range(0, 9):
        fish_dict[num] = 0
    for fish in data:
        fish_dict[fish] += 1
    
    # sorted_fish = sorted(fish_dict.items())
    # print(f"Init: {sorted_fish}")

    # Generate new values
    copy_dict = {}

    for day in range(1, num_days+1):
        zero_val = fish_dict[0]
        for idx in range(1, 9):
            copy_dict[idx - 1] = fish_dict[idx]
        copy_dict[8] = zero_val
        copy_dict[6] += zero_val

        # Copy dictionary and print sorted list
        fish_dict = copy_dict
        
        # sorted_fish = sorted(fish_dict.items())
        # print(f"Day{day}: {sorted_fish}")
 
    return returnSum(fish_dict)
    
# Return the sum of the values in the dictionary
def returnSum(fish_dict):
    sum = 0
    for i in fish_dict.values():
        sum = sum + i

    return sum

# --- Answer ---
# print(f"Part 1: {part_one(data)}")
print(f"Part 2: {part_two(data)}")