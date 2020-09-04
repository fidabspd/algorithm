board1 = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]  # 9
board2 = [[0,0,1,1],[1,1,1,1]]  # 4

def solution(board):

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

print(solution(board1))
print(solution(board2))