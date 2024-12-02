sample_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

with (open("day4.txt", "r")) as f:
    sample_input = f.read()


def print_board(b):
    for line in b[0]:
        print(" ".join([str(x) for x in line]))
    for line in b[1]:
        print(" ".join([str(x) for x in line]))

def check_board(b):
    b = b[0]
    cols = [True for r in range(len(b[0]))]
    for r in range(len(b)):
        if all(b[r]):
            return True
        for c in range(len(b[r])):
            # print(f"col[c] is {col[c]} and is being &d with {b[r][c]}")
            cols[c] = cols[c] & b[r][c]
    return any(cols)

def score_board(b):
    bsum = 0
    for r in range(len(b[0])):
        for c in range(len(b[0][r])):
            if not b[0][r][c]:
                bsum += int(b[1][r][c])
    return bsum

number_list, *board_numbers = sample_input.split("\n\n")

boards = [([[False]*5 for _ in range(5)], [[y for y in x.split(" ") if y != ''] for x in board.split("\n")]) for board in board_numbers]
numbers = [x for x in number_list.split(",")]


indx = 0
winners = []
winner = None
last_num = None
for number in numbers:
    last_num = number
    for board in boards:
        for i, row in enumerate(board[1]):
            for j, col in enumerate(row):
                if col == number:
                    board[0][i][j] = True

    for board in boards:
        if not board in winners:
            if check_board(board):
                winners.append(board)
    if len(winners) == len(boards):
        winner = winners[-1]
        break
            
print_board(winner)
print(score_board(winner), number)
print(score_board(winner) * int(number))


