# 6:23
def fill_row(row):
    curr = '?'
    for i in range(len(row)):
        if row[i] == '?':
            row[i] = curr
        else:
            curr = row[i]
    for i in range(len(row) - 1, -1, -1):
        if row[i] == '?':
            row[i] = curr
        else:
            curr = row[i]
    return row


def solution(board, rows, cols):
    for i in range(rows):
        board[i] = fill_row(board[i])
    board = [[row[i] for row in board] for i in range(cols)]

    for i in range(cols):
        board[i] = fill_row(board[i])
    board = [[row[i] for row in board] for i in range(rows)]
    return board


path = '/home/dzhang379/Downloads/'
fname = input()

with open(path + fname, 'r') as f, open(path + fname[:-3] + '.out', 'w+') as out:
    t = int(f.readline().strip())
    for i in range(1, t + 1):
        rows, cols = [int(s) for s in (f.readline().strip()).split(' ')]
        board = [[0]*rows for i in range(rows)]

        for row in range(rows):
            board[row] = [s for s in (f.readline().strip())]

        cake = solution(board, rows, cols)
        out.write("Case #{}: \n".format(i))

        for row in cake:
            out.write(''.join(row) + '\n')
