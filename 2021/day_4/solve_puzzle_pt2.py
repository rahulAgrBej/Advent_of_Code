
import pprint

pp = pprint.PrettyPrinter(indent=3)

# returns list of char nums in line
def process_line(line):

    nums = []

    # check for empty space at the beginning first and correct
    if line[0] == ' ':
        line = line[1:]

    curr_num = ''

    for idx in range(len(line)):

        if line[idx] == ' ':
            if len(curr_num) > 0:
                nums.append(curr_num)
            curr_num = ''
        else:
            curr_num += line[idx]
    
    if len(curr_num) > 0:
        nums.append(curr_num)
        
    return nums

def update_lookup(num_lookup, board_num, row_num, row):

    for num_idx in range(len(row)):
        curr_num = row[num_idx]
        if not(curr_num in num_lookup):
            num_lookup[curr_num] = []
        
        num_lookup[curr_num].append((board_num, row_num, num_idx))
    
    return num_lookup

def preprocess_input(input):

    input = input.split('\n')

    # get bingo numbers
    bingo_nums = input[0].split(',')

    # number lookups
    # nums will be stored as tuples of (board number, row number, column number)
    num_lookup = {}

    new_matrix = False

    boards = []
    curr_board = []
    board_num = 0
    row_num = 0

    # get bingo boards 5 x 5 matrices
    for line in input[2:]:

        # new matrix 
        if len(line) == 0:
            boards.append(curr_board)
            curr_board = []
            board_num += 1
            row_num = 0
        else:
            row = process_line(line)
            curr_board.append(row)
            num_lookup = update_lookup(num_lookup, board_num, row_num, row)
            row_num += 1
    
    if len(curr_board) > 0:
        boards.append(curr_board)

    return bingo_nums, boards, num_lookup

def check_row(row, marker):

    solved = True

    for idx in range(len(row)):
        if row[idx] != marker:
            solved = False
            break
    
    return solved

def check_solution(board, marker, row_idx, col_idx):

    # check row
    row = board[row_idx]
    row_solution = check_row(row, marker)

    # check column
    column = []
    for idx in range(len(board)):
        col_num = board[idx][col_idx]
        column.append(col_num)

    col_solution = check_row(column, marker)

    return (row_solution or col_solution)

def update_boards(boards, available_boards, bingo_num, num_lookup, marker):

    solution = False
    board_solution_idx = -1
    solved_indices = []

    for num_occurence  in num_lookup[bingo_num]:
        board_idx = num_occurence[0]
        board_idx = available_boards[board_idx]

        if board_idx > -1:
            row_idx = num_occurence[1]
            col_idx = num_occurence[2]

            # mark number on board
            boards[board_idx][row_idx][col_idx] = marker
            
            # check if a solution occured
            board = boards[board_idx]
            solution = check_solution(board, marker, row_idx, col_idx)

            if solution:
                solved_indices.append(board_idx) 

    return boards, solved_indices

def sum_board(board, marker):

    total = 0

    for row_idx in range(len(board)):
        for col_idx in range(len(board[row_idx])):
            if board[row_idx][col_idx] != marker:
                total += int(board[row_idx][col_idx])
    
    return total

f = open('inputs/input.txt', 'r')
input = f.read()
f.close()

bingo_nums, boards, num_lookup = preprocess_input(input)

marker = 'X'
final_board_idx = -1
final_bingo_num = -1

available_boards = list(range(len(boards)))
last_solved_board = (-1, -1)

for bingo_num in bingo_nums:
    print(bingo_num)
    pp.pprint(boards[1])

    boards, solved_indices = update_boards(boards, available_boards, bingo_num, num_lookup, marker)

    # if solution found
    for solved_idx in solved_indices:
        available_boards[solved_idx] = -1
    
    if sum(available_boards) == (-1 * len(available_boards)):
        last_board_idx = solved_indices[-1]
        last_final_bingo_num = bingo_num
        break
        

last_board_total = sum_board(boards[last_board_idx], marker)
last_final_bingo_num = int(last_final_bingo_num)

print(f'Board Total: {last_board_total}')
print(f'Bingo Number: {last_final_bingo_num}')
print(f'Board Total * bingo num: {last_board_total * last_final_bingo_num}')
