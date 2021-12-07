#     --- Day 4: Giant Squid ---
#     https://adventofcode.com/2021/day/4

# --- Handle input file ---
file = open("input4.txt", 'r')
pulled_numbers = file.readline()

boards = file.readlines()
boards = [line.rstrip('\n') for line in boards]
boards = [line.split(' ') for line in boards]

class Bingo_board:
    def __init__(self, id, row_board, col_board):
        self.id = id
        self.row_board = row_board
        self.col_board = col_board

    def __str__(self):
        return f'Bingo_board(ID: {self.id},\n{self.row_board[0]}\n{self.row_board[1]}\n \
            {self.row_board[2]}\n{self.row_board[3]}\n{self.row_board[4]})'
    
    def draw_number(self, pulled_number) -> int:      
        for row in self.row_board:
            if pulled_number in row:
                row.remove(pulled_number)
        for col in self.col_board:    
            if pulled_number in col:
                col.remove(pulled_number)

        for row in self.row_board:
            if len(row) == 0:
                return self.id
            
        for col in self.col_board:
            if len(col) == 0:
                return self.id
            else: 
                return -1
    
    def get_board_sum(self) -> int:
        total = 0
        for row in self.row_board:
            total += sum(row)
        return total

    def get_id(self) -> int:
        return self.id

example_numbers = "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1"
example_boards = [
    ['22', '13', '17', '11', '0'],
    ['8', '2', '23', '4', '24'],
    ['21', '9', '14', '16', '7'],
    ['6', '10', '3', '18', '5'],
    ['1', '12', '20', '15', '19'],
    ['3', '15', '0', '2', '22'],
    ['9', '18', '13', '17', '5'],
    ['19', '8', '7', '25', '23'],
    ['20', '11', '10', '24', '4'],
    ['14', '21', '16', '12', '6'],
    ['14', '21', '17', '24', '4'],
    ['10', '16', '15', '9', '19'],
    ['18', '8', '23', '26', '20'],
    ['22', '11', '13', '6', '5'],
    ['2', '0', '12', '3', '7'],
]

# --- Returns the score of the board which finished in the requested position ---
def winning_board(pulled_numbers, boards):
    bingo_boards = []
    win_order = []
    board_totals = []
    winning_numbers = []
    data = parse_input(boards)

    pulled_numbers = pulled_numbers.split(',')
    pulled_numbers = [int(x) for x in pulled_numbers]

    # Fill bingo_boards list with Bingo_board class instances
    for idx, board in enumerate(data):
        bingo_boards.append(Bingo_board(idx+1, board, make_col_board(board)))
    
    for number in pulled_numbers:
        for board in bingo_boards:
            if board.draw_number(number) > -1:
                win_order.append(board.get_id())
                board_totals.append(board.get_board_sum())
                winning_numbers.append(number)
                print(f"Board ID: {board.get_id()}   Board Value: {board.get_board_sum()}   Winning number: {number}   Total Score:  {board.get_board_sum()*number}")
                bingo_boards.remove(board)                

    print(f"Part 1: {winning_numbers[0]*board_totals[0]}")
    print(f"Part 2:  {winning_numbers[len(winning_numbers)-1]*board_totals[len(board_totals)-1]}")
    
# --- Helper Functions ---

# Delete multiple elements of a list
# https://thispointer.com/python-remove-elements-from-list-by-index/
def delete_mult(list_object, indices):
    indices = sorted(indices, reverse=True)
    for idx in indices:
        if idx < len(list_object):
            list_object.pop(idx)

# Parse Input
def parse_input(boards) -> list:
    del_list = []
    for x in range(len(boards)):
        if x % 6 == 0:
            del_list.append(x)
    delete_mult(boards, del_list)

    # Delete empty strings in lists
    for group in boards:
        while "" in group:
            group.remove("")

    # Convert strings to int
    boards = [[int(i) for i in group] for group in boards]

    # Group lines into boards
    lower = 0
    upper = 5
    num_boards = int(len(boards)/5)
    grouped_boards = []
    for idx in range(num_boards):
        grouped_boards.append([])
        for jdx in range(lower, upper):
            grouped_boards[idx].append(boards[jdx])
        lower += 5
        upper += 5

    return(grouped_boards)

# Make Column Board
def make_col_board(board) -> list:
    col_board = [[],[],[],[],[]]
    
    for row in board:
        for idx in range(len(row)):
            col_board[idx].append(row[idx])
    
    return col_board

# --- Answer ---
print("[REAL DATA]")
winning_board(pulled_numbers, boards)
print("[EXAMPLE]")
winning_board(example_numbers, example_boards)

# --- Close File ---
file.close()