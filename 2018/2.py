#     --- Day 2: Inventory Management System ---
#     https://adventofcode.com/2018/day/2

from collections import Counter

with open("input2.txt", 'r') as file:
    data = [line.strip() for line in file]

# --- Example Data ---
example1 = [
    'abcdef',
    'bababc',
    'abbcde',
    'abcccd',
    'aabcdd',
    'abcdee',
    'ababab',
]

example2 = [
    'abcde',
    'fghij',
    'klmno',
    'pqrst',
    'fguij',
    'axcye',
    'wvxyz',
]

# --- Part 1 ---
def part_1(data) -> int:  
    doubles = 0
    triples = 0
    
    for box in data:
        chars = {}
        for x in box:
            chars[x] = chars.get(x, 0) + 1
        if 2 in chars.values():
            doubles += 1
        if 3 in chars.values():
            triples += 1
    return doubles * triples

# --- Part 2 ---
def part_2(data) -> str:
    answers = []
    
    for idx, code1 in enumerate(data):
        for jdx, _ in enumerate(data):
            dif = 0
            for val in range(len(code1)):
                if code1[val] != data[jdx][val]:
                    dif += 1
            if dif == 1:
                answers.append(code1)

    for idx in range(len(answers[0])):
        if answers[0][idx] != answers[1][idx]:
            final_answer = answers[0][0 : idx : ] + answers[0][idx + 1 : :]
            
    return final_answer          

# --- Testing ---
assert (part_1(example1)) == 12
assert (part_2(example2)) == "fgij"

# --- Answer ---
print(f"Part 1: {part_1(data)}")
print(f"Part 2: {part_2(data)}")