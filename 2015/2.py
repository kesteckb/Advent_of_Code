#     --- Day 2: I Was Told There Would Be No Math ---
#     https://adventofcode.com/2015/day/2

# Read in file
newList = []
with open("input2.txt") as file:
    dimensions = file.readlines()
for element in dimensions:
    newList.append(element.strip('\n').split('x'))

# --- Part 1 ---
def part_1(newList) -> int:
    surface_area = 0

    for set in newList:
        length = int(set[0])
        width = int(set[1])
        height = int(set[2])

        side1 = length*width
        side2 = width*height
        side3 = height*length

        if side1 <= side2 and side1 <= side3:
            extra = side1
        elif side2 <= side1 and side2 <= side3:
            extra = side2
        else:
            extra = side3

        surface_area += (2*side1) + (2*side2) + (2*side3) + extra
    return surface_area

# --- Part 2 ---
def part_2(newList) -> int:
    wrap = 0
    bow = 0
    
    for set in newList:
        length = int(set[0])
        width = int(set[1])
        height = int(set[2])
        bow += length*width*height

        if length <= width and length <= height:
            side1 = length
        elif width <= length and width <= height:
            side1 = width
        else:
            side1 = height
        if (length <= width and length >= height) or (length >= width and length <= height):
            side2 = length
        elif (width <= length and width >= height) or (width >= length and width <= height):
            side2 = width
        else:
            side2 = height

        wrap += (side1*2) + (side2*2)

    return wrap+bow

# Answer
print(f"Part 1: {part_1(newList)}")
print(f"Part 2: {part_2(newList)}")

# Close file
file.close()