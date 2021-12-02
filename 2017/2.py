#     --- Day 2: Corruption Checksum ---
#     https://adventofcode.com/2017/day/2

# Read in the data
with open("input2.txt", 'r') as file:   
    data = [[int(x) for x in line.split("\t")] for line in file]

# --- Part 1 ---
def part_1(data) -> int:
    checksum = 0

    for set in data:
        min = 9999
        max = -1
        for number in set:
            if number < min:
                min = number
            if number > max:
                max = number
        checksum += (max - min)
    return checksum

# --- Part 2 ---
def part_2(data) -> int:
    sum = 0
    for set in data:
        end = len(set) - 1
        for idx in range(len(set)):
            for idx2 in range(len(set)):
                if (end - idx2) > idx:
                    remainder1 = set[idx] % (set[end - idx2])
                    remainder2 = (set[end - idx2]) % set[idx]
                    if remainder1 == 0:
                        sum += set[idx] / (set[end - idx2])
                    if remainder2 == 0:
                        sum += (set[end - idx2]) / set[idx]
    return sum

# Test Part 1
test_data = [
    [5,1,9,5],
    [7,5,3],
    [2,4,6,8],
]
assert part_1(test_data) == 18

# Test Part 2
test_data2 = [
    [5,9,2,8],
    [9,4,7,3],
    [3,8,6,5],
]
assert part_2(test_data2) == 9

# Answer
print("Part 1: " + str(part_1(data)))
print("Part 2: " + str(part_2(data)))