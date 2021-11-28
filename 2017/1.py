#     --- Day 1: Inverse Captcha ---
#     https://adventofcode.com/2017/day/1

# Read in the data
file = open("input1.txt", 'r')
data = file.readline().strip()

# ---Part 1---
def part1(data) -> int:
    sum = 0
    for idx in range(len(data)):
        if idx < (len(data) - 1):
            if data[idx] == data[idx+1]:
                sum += int(data[idx])
        elif idx == (len(data) - 1):
            if data[idx] == data[0]:
                sum += int(data[idx])
    return sum

# ---Part 2---
def part2(data) -> int:
    sum = 0
    half = int(len(data)/2)

    for idx in range(len(data)):
        if idx < half:
            if data[idx] == data[idx + half]:
                sum += int(data[idx])
        else:
            if data[idx] == data[idx - half]:
                sum += int(data[idx])
    return sum

# Test Part 1
assert part1("1122") == 3
assert part1("1111") == 4
assert part1("1234") == 0
assert part1("91212129") == 9

# Test Part 2
assert part2("1212") == 6
assert part2("1221") == 0
assert part2("123425") == 4
assert part2("123123") == 12
assert part2("12131415") == 4

# Answer
print("Part 1: " + str(part1(data)))
print("Part 2: " + str(part2(data)))

# Close the file
file.close()