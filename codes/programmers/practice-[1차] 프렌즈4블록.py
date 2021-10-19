m1 = 4; n1 = 5; board1 = ["CCBDE", "AAADE", "AAABF", "CCBBF"]  # 14
m2 = 6; n2 = 6; board2 = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]  # 15


def solution(m, n, board):
    board = [list(col) for col in zip(*board)]
    while True:
        erase = []
        for col in range(n-1):
            for row in range(m-1):
                square = board[col][row:row+2] + board[col+1][row:row+2]
                if '' in square:
                    continue
                if len(set(square)) == 1:
                    erase.extend([(row, col), (row+1, col), (row, col+1), (row+1, col+1)])
        if not erase:
            break
        for row, col in erase:
            board[col][row] = ''
        board = list(map(lambda x: sorted(x, key=lambda e: e == '', reverse=True), board))
    return sum(map(lambda x: m-len(''.join(x)), board))
    

print(solution(m1, n1, board1))
print(solution(m2, n2, board2))
