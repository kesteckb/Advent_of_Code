#     --- Day 2: Corruption Checksum ---
#     https://adventofcode.com/2017/day/2

# Read in the data
file = open("input2.txt", 'r')
data = file.read().replace("\n", "\t").split("\t")

print(data)

# --- Part 1 ---
def part_1(data) -> int:
    checksum = 0

    for number in data:
        min = 10
        max = -1
        
        for idx in range(len(number)):
            value = int(number[idx])
            if value < min:
                min = value
            if value > max:
                max = value
        checksum += (max - min)
        print("number: " + number + "   difference: " + str(max - min))
    return checksum

# Test Part 1
# test_data = [
#     '5195',
#     '753',
#     '2468',
# ]
# assert part_1(test_data) == 18

# Answer
print("Part 1: " + str(part_1(data)))
#1305 is wrong

# Close the file
file.close()