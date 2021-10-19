board1 = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]  # 9
board2 = [[0,0,1,1],[1,1,1,1]]  # 4


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
def solution(board):
    board = np.array(board)
    size_max = min(board.shape)
    for size in range(size_max, 0, -1):
        for r in range(board.shape[0]-size+1):
            for c in range(board.shape[1]-size+1):
                if sum(board[r:r+size, c:c+size].reshape(-1)) == size**2:
                    return size**2
    return 0


print(solution(board1))
print(solution(board2))