#     --- Day 2: Bathroom Security ---
#     https://adventofcode.com/2016/day/2

# Read from file
with open("input2.txt", 'r') as file:
    lines = [line.rstrip() for line in file]

example = [
    'ULL',
    'RRDDD',
    'LURDL',
    'UUUUD',
]

keypad = {
    '1': (0, 2),
    '2': (-1, 1),
    '3': (0, 1),
    '4': (1, 1),
    '5': (-2, 0),
    '6': (-1, 0),
    '7': (0, 0),
    '8': (1, 0),
    '9': (2, 0),
    'A': (-1, -1),
    'B': (0, -1),
    'C': (1, -1),
    'D': (0, -2),
}
key_list = list(keypad.keys())
val_list = list(keypad.values())

def part_1(lines) -> str:
    code = []
    on = 5

    for line in lines:
        for command in line:
            if command == 'L':
                on = move_left(on)
            elif command == 'R':
                on = move_right(on)
            elif command == 'U':
                on = move_up(on)
            elif command == 'D':
                on = move_down(on)
            else:
                raise RuntimeError(f"Got unexpected token")
        code.append(on)
    code_str = ''.join(map(str, code))
    return code_str

def part_2(lines) -> str:
    code = []
    key = '5'

    for line in lines:
        for command in line:
            if command == 'L':
                key = move_left_p2(key)
            elif command == 'R':
                key = move_right_p2(key)
            elif command == 'U':
                key = move_up_p2(key)
            elif command == 'D':
                key = move_down_p2(key)
            else:
                raise RuntimeError(f"Got unexpected token")
        code.append(key)
    code_str = ''.join(map(str, code))
    return code_str

def move_left_p2(key) -> str:
    if key == '1' or key == '2' or key == '5' or key == 'A' or key == 'D':
        return key
    else:
        coord = keypad[key][0]
        coord -= 1
        position = val_list.index((coord, keypad[key][1]))
        return key_list[position]

def move_right_p2(key) ->str:
    if key == '1' or key == '4' or key == '9' or key == 'C' or key == 'D':
        return key
    else:
        coord = keypad[key][0]
        coord += 1
        position = val_list.index((coord, keypad[key][1]))
        return key_list[position]

def move_up_p2(key) ->str:
    if key == '5' or key == '2' or key == '1' or key == '4' or key == '9':
        return key
    else:
        coord = keypad[key][1]
        coord += 1
        position = val_list.index((keypad[key][0], coord))
        return key_list[position]

def move_down_p2(key) ->str:
    if key == '5' or key == 'A' or key == 'D' or key == 'C' or key == '9':
        return key
    else:
        coord = keypad[key][1]
        coord -= 1
        position = val_list.index((keypad[key][0], coord))
        return key_list[position]

def move_left(number) -> int:
    if number == 1 or number == 4 or number == 7:
        return number
    else:
        return number-1

def move_right(number) ->int:
    if number == 3 or number == 6 or number == 9:
        return number
    else:
        return number+1

def move_up(number) ->int:
    if number > 0 and number < 4 :
        return number
    else:
        return number-3

def move_down(number) ->int:
    if number > 6 and number < 10:
        return number
    else:
        return number+3

# --- Test Part 1 ---
assert part_1(example) == "1985"
# --- Test Part 2 ---
assert part_2(example) == "5DB3"

# --- Answer ---
print(f"Part 1: {part_1(lines)}")
print(f"Part 2: {part_2(lines)}")

# Close file
file.close()