#     --- Day 1: Not Quite Lisp ---
#     https://adventofcode.com/2015/day/1

# Read in the data
file = open("input1.txt", 'r')
input = file.read()

# --- Part 1 ---
def part_1(input) -> int:
    floor = 0

    for x in input:
        if x == "(":
            floor += 1
        elif x == ")":
            floor -= 1

    return floor

# --- Part 2 ---
def part_2(input) -> int:
    floor = 0
    count =0

    for x in input:
        count += 1
        if x == "(":
            floor += 1
        elif x == ")":
            floor -= 1
        if floor < 0:
            return count
    return -1

# Test Part 1
assert part_1("(())") == 0
assert part_1("()()") == 0
assert part_1("(((") == 3
assert part_1("(()(()(") == 3
assert part_1("))(((((") == 3
assert part_1("())") == -1
assert part_1("))(") == -1
assert part_1(")))") == -3
assert part_1(")())())") == -3

# Answer
print(f"Part 1: {part_1(input)}")
answer2 = part_2(input)
if answer2 == -1:
    print("Santa never enters the basement!")
print(f"Part 2: {answer2}")

# Close file
file.close()