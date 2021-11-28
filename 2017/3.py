#     --- Day 3: Spiral Memory ---
#     https://adventofcode.com/2017/day/3

# 1^1 ... 3^2 ... 5^2 ... 7^2
#  3       2       1       0

input = 368078

def part_1(input) -> int:
    if input == 1:
        return 0

    edge = 1

    while edge**2 <= input:
        edge += 2

    low = pow(edge-2, 2) + 1
    high = pow(edge, 2)

    x, y = edge//2, -(edge//2)
    print(x, y)
    while high > input and x > -(edge//2):
        high -= 1
        x -= 1
    
    while high > input and y < edge//2:
        high -= 1
        y += 1
    
    while high > input and x < edge//2:
        high -= 1
        x += 1
    
    while high > input and y > -(edge//2):
        high -= 1
        y -= 1
    
    print(x, y)
    return abs(x) + abs(y)

print(f"Part 1: {part_1(input)}")