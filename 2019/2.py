#     --- Day 2: 1202 Program Alarm ---
#     https://adventofcode.com/2019/day/2

# --- Read in data from file ---
with open("input2.txt", 'r') as file:
    data = [int(num) for num in file.readline().split(',')]

# --- Example ---
example = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]

# --- Part 1 ---
def part_one(part_1_data):
    part_1_data = data
    
    for idx, number in enumerate(part_1_data):
        position = idx + 1
        if (position) % 4 == 0:
            one = part_1_data[idx - 3]
            two = part_1_data[idx - 2]
            three = part_1_data[idx - 1]
            four = part_1_data[idx]
            if one == 1:
                value = add(part_1_data[two], part_1_data[three])
            elif one == 2:
                value = multiply(part_1_data[two], part_1_data[three])
            elif one == 99:
                break
            else:
                raise RuntimeError(f"Got unexpected token")
            
            part_1_data[four] = value
            part_1_data[1] = 12
            part_1_data[2] = 2
            
    return part_1_data

# --- Part 2 ---
def part_two(data) -> int:
    

def add(operand1, operand2) -> int:
    return operand1 + operand2

def multiply(operand1, operand2) -> int:
    return operand1 * operand2

# --- Answer ---
new_list = part_one(example)
answer = new_list[0]
print(f"Part 1: {answer}")