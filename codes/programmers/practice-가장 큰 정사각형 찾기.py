board1 = [
    [0,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [0,0,1,0]
]  # 9
board2 = [
    [0,0,1,1],
    [1,1,1,1]
]  # 4


def solution_0(board):

    answer = 0

    for i in range(1, min(len(board), len(board[0]))+1):
        for r in range(len(board) - i + 1):
            for c in range(len(board[0]) - i + 1):

                if board[r][c] == 0:
                    continue

                tmp = 0
                for j in range(i):
                    #print(board[r+j][c:c+i])
                    tmp += sum(board[r+j][c:c+i])
                #print(tmp, tmp == i**2, '\n')

                if tmp == i**2 and tmp > answer:
                    answer = tmp

    return answer


import numpy as np
def solution_1(board):
    board = np.array(board)
    size_max = min(board.shape)
    for size in range(size_max, 0, -1):
        for r in range(board.shape[0]-size+1):
            for c in range(board.shape[1]-size+1):
                if sum(board[r:r+size, c:c+size].reshape(-1)) == size**2:
                    return size**2
    return 0


def solution_2(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            print('\n', i, j, sep='')
            if board[i][j] == 0:
                continue
            answer_tmp = 1
            for l in range(1, min(len(board), len(board[0]))+1):
                if l+i > len(board) or l+j > len(board[0]):
                    break
                print(l)
                sq = 0
                for r in range(l):
                    print(board[i+r][j:j+l])
                    sq += sum(board[i+r][j:j+l])
                if sq != l**2:
                    print('break')
                    break
                answer_tmp = sq
            if answer_tmp > answer:
                answer = answer_tmp
    return answer


def solution(board):
    answer = 0
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 0:
                continue
            board[i][j] += min(board[i-1][j-1], board[i-1][j], board[i][j-1])
            if board[i][j] > answer:
                answer = board[i][j]
    if answer == 0:
        answer = max([max(b) for b in board])
    return answer**2

print(solution(board1))
print(solution(board2))