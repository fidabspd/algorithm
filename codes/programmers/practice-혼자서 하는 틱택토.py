board0 = ["O.X", ".O.", "..X"]  # 1
board1 = ["OOO", "...", "XXX"]  # 0
board2 = ["...", ".X.", "..."]  # 0
board3 = ["...", "...", "..."]  # 1


def solution(board):
    board = "".join(board)
    countO = board.count("O")
    countX = board.count("X")
    count_diff = countO - countX
    if count_diff not in [0, 1]:
        return 0
    checks = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    checkO = 0
    checkX = 0
    for c in checks:
        tmp = "".join([board[i] for i in c])
        if tmp == "OOO":
            checkO += 1
            if count_diff == 0:
                return 0
        elif tmp == "XXX":
            checkX += 1
            if count_diff == 1:
                return 0
        if checkO == 2:
            return 1
        if checkX > 1:
            return 0
    return 1


print(solution(board0))
print(solution(board1))
print(solution(board2))
print(solution(board3))
