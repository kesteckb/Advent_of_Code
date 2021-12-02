#     --- Day 4: High-Entropy Passphrases ---
#     https://adventofcode.com/2017/day/4

# Read in the data
with open("input4.txt", 'r') as file:   
    data = [[x for x in line.strip('\n').split(" ")] for line in file]

# --- Part 1 ---
def part_1(data) -> int:
    return len([password for password in data if is_valid(password)])
    
    # good_pw = 0

    # for password in data:
    #     if is_valid(password):
    #         good_pw += 1
    # return good_pw

# --- Part 2 ---
def part_2(data) -> int:
    valid_passwords = []

    for password in data:
        seen = set()
        pw_invalid = False
        for word in password:
            if "".join(sorted(word)) in seen:
                pw_invalid = True
            seen.add("".join(sorted(word)))
        if pw_invalid == False:
            valid_passwords.append(password)    

    return len(valid_passwords)

# Returns True if a password has no duplicate strings, otherwise returns False
def is_valid(password) -> bool:
    return len(password) == len(set(password))

# Test Part 1
assert is_valid(['aa', 'bb', 'cc', 'dd', 'ee']) == True
assert is_valid(['aa', 'bb', 'cc', 'dd', 'aa']) == False
assert is_valid(['aa', 'bb', 'cc', 'dd', 'aaa']) == True

# Answer
print(f"Part 1: {part_1(data)}")
print(f"Part 2: {part_2(data)}")