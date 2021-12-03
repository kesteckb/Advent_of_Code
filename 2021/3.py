#     --- Day 3: Binary Diagnostic ---
#     https://adventofcode.com/2021/day/3

from collections import Counter
from collections import deque

# --- Get Input ---
with open("input3.txt", 'r') as file:
    data = [line.strip('\n') for line in file]

# --- Sample Data ---
example = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010',
]

# --- Part 1 ---
def part_1(data) -> int:
    gamma = ""
    for idx in range(len(data[0])):
        column_string = ""
        for binary in data:
            column_string = column_string + binary[idx]
        cnt = Counter(column_string).most_common(1)
        popped = deque(cnt).popleft()
        gamma = gamma + popped[0]
    epsilon = get_epsilon(gamma)

    return bin_to_dec(gamma) * bin_to_dec(epsilon)

# --- Part 2 ---
def part_2(data) -> int:
    ox_list = []
    co2_list = []

    for line in data:
        ox_list.append(line)
        co2_list.append(line)

    # Oxygen Generator Rating   
    while len(ox_list) > 1:
        # For each Column in data get the value from each row
        for idx in range(len(ox_list[0])):
            column = ""
            most_common = None
            for line in ox_list:
                column = column + line[idx]
            
            # Get most common binary occurance
            # Check if all values in column are the same
            if len(co2_list) > 1: 
                frequency = Counter(column).most_common(2)

                if frequency[0][1] == frequency[1][1]:
                    most_common = '1'
                else:
                    most_common = frequency[0][0]

                # Get indices of rows to delete
                del_list = []
                
                for row, line in enumerate(ox_list):
                    if line[idx] != most_common:
                        del_list.append(row)
                
                # Delete rows
                if len(del_list) != len(ox_list):
                    delete_mult(ox_list, del_list)

    # CO2 Scrubber Rating
    while len(co2_list) > 1:
        # For each Column in data get the value from each row
        for idx in range(len(co2_list[0])):
            column = ""
            most_common = None
            for line in co2_list:
                column = column + line[idx]

            # Get most common binary occurance
            # Check if all values in column are the same
            if len(co2_list) > 1: 
                frequency = Counter(column).most_common(2)
                if frequency[0][1] == frequency[1][1]:
                    least_common = '0'
                else:
                    least_common = frequency[1][0]

                # Get indices of rows to delete
                del_list = []

                for row, line in enumerate(co2_list):
                    if line[idx] != least_common:
                        del_list.append(row)
                # Delete rows
                if len(del_list) != len(co2_list):
                    delete_mult(co2_list, del_list)

    oxygen_generator_rating =  bin_to_dec(ox_list[0])
    co2_scrubber_rating =  bin_to_dec(co2_list[0])

    return oxygen_generator_rating * co2_scrubber_rating

# Delete multiple elements of a list 
# https://thispointer.com/python-remove-elements-from-list-by-index/
def delete_mult(list_object, indices):
    indices = sorted(indices, reverse=True)
    for idx in indices:
        if idx < len(list_object):
            list_object.pop(idx)

# Convert Binary to Decimal
def bin_to_dec(binary) -> int:
    return int(binary, 2)

# Convert Gamma to Epsilon
def get_epsilon(gamma) -> str:
    epsilon = gamma.replace('1', '2')
    epsilon = epsilon.replace('0', '1')
    epsilon = epsilon.replace('2', '0')
    return epsilon

# --- Testing ---
assert part_1(example) == 198

# --- Answer ---
print(f"Part 1: {part_1(data)}")
print(f"Part 2: {part_2(data)}")