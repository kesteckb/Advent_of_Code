#     --- Day 3: Squares With Three Sides ---
#     https://adventofcode.com/2016/day/3

with open("input3.txt", 'r') as file:
    lines = [[int(x) for x in line.strip().split()] for line in file]

# --- Part 1 ---
def part_1(lines) -> int:
    triangles = 0

    # return len([line for line in lines if sum(line) - 2 * max(line) > 0])
    for line in lines:
        if sum(line) - (2*max(line)) > 0:
            triangles += 1
    return triangles

# --- Part 2 ---
def part_2(lines) -> int:
    triangles = 0

    for idx, _ in enumerate(lines):        
        left = []
        center = []
        right = []
        
        if (idx + 1) % 3 == 0:
            for num in range(0, 3):
                left.append(lines[idx-num][0])
                center.append(lines[idx-num][1])
                right.append(lines[idx-num][2])
            triangles += check_triangle(left) + check_triangle(center) + check_triangle(right)
    return triangles
            
def check_triangle(triangle) -> int:
    if sum(triangle) - 2 * max(triangle) > 0:
        return 1
    return 0

# --- Answer ---
print(f"Part 1: {part_1(lines)}")
print(f"Part 2: {part_2(lines)}")