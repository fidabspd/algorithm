# def solution(board, moves):
#     answer = 0
#     return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
# result = 4

def solution(board, moves):
    board_T = []
    for id in range(len(board)):
        col = []
        for row in board:
            if row[id] != 0:
                col.append(row[id])
        board_T.append(col)

    des = []
    result = 0
    for move in moves:
        if len(board_T[move-1]) > 0:
            tmp = board_T[move-1].pop(0)
            des.append(tmp)
            if len(des) > 1:
                if des[-2] == tmp:
                    des.pop(); des.pop()
                    result += 2
    return result
        
print(solution(board, moves))