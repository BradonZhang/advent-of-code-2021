import numpy as np

with open('in/4.txt') as f:
    blocks = f.read().strip().split('\n\n')
    draw_nums = [int(x) for x in blocks.pop(0).split(',')]

def make_boards():
    return [np.array([[int(x) for x in row.split()] for row in block.splitlines()]) for block in blocks]

def mark_board(board, num):
    w = np.transpose(np.where(board == num))
    if not len(w):
        return
    board[tuple(w[0])] = ~board[tuple(w[0])]

def has_bingo(board):
    col_counts = [0] * 5
    for i, row in enumerate(board):
        row_count = 0
        for j, cell in enumerate(row):
            if cell >= 0:
                continue
            row_count += 1
            col_counts[j] += 1
        if row_count == 5:
            return True
    return max(col_counts) >= 5

def score(board, num):
    return num * sum(board[board >= 0])


# Part 1

boards = make_boards()

for num in draw_nums:
    for board in boards:
        mark_board(board, num)
        if has_bingo(board):
            print(score(board, num))
            break
    else:
        continue
    break


# Part 2

boards = make_boards()
last_score = None
done = set()

for num in draw_nums:
    for i, board in enumerate(boards):
        if i in done:
            continue
        mark_board(board, num)
        if has_bingo(board):
            last_score = score(board, num)
            done.add(i)

print(last_score)
