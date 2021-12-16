#     --- Day 4: Security Through Obscurity ---
#     https://adventofcode.com/2016/day/4

with open("test_input4.txt", 'r') as file:
    data = [line.strip().split('-') for line in file.readlines()]

example = [
    ['aaaaa, bbb, z, y, x, 123[abxyz]'],
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', '987[abcde]'],
    ['not', 'a', 'real', 'room', '404[oarel]'],
    ['totally', 'real', 'room', '200[decoy]'],
]

def part_one(data):
    

