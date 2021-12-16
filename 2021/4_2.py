#     --- Day 4: Giant Squid ---
#     https://adventofcode.com/2021/day/4

with open("input4.txt", 'r') as file:
    numbers = [int(x) for x in file.readline().split(',')]
    file.readline()
    datasets = [x for x in file.readlines()]

example_draw = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]


print(datasets)