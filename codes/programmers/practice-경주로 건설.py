# https://school.programmers.co.kr/learn/courses/30/lessons/67259

board0 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]  # 900
board1 = [
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
]  # 3800
board2 = [
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [1, 0, 0, 0],
]  # 2100
board3 = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
]  # 3200


def solution(board):
    from collections import deque

    def check(i, j):
        if i == 0 and j == 0:
            return False
        if not 0 <= i < len_board:
            return False
        if not 0 <= j < len_board:
            return False
        if board[i][j] == 1:
            return False
        return True

    def get_neighbor(i, j):
        return [pos for pos in [(i, j - 1), (i + 1, j), (i, j + 1), (i - 1, j)]]

    len_board = len(board)
    cost_board = [[[-1] * 4 for _ in range(len_board)] for _ in range(len_board)]
    queue = deque([(0, 0, -1, 0)])  # i, j, direction, cost
    while queue:
        i_prev, j_prev, direction_prev, cost_prev = queue.popleft()
        for direction_new, (i_new, j_new) in enumerate(get_neighbor(i_prev, j_prev)):
            if not check(i_new, j_new):
                continue
            if direction_prev == -1 or direction_prev == direction_new:
                cost_add = 100
            elif abs(direction_prev - direction_new) != 2:
                cost_add = 600
            else:
                continue
            cost_new = cost_prev + cost_add
            if cost_board[i_new][j_new][direction_new] != -1 and cost_board[i_new][j_new][direction_new] <= cost_new:
                continue
            queue.append((i_new, j_new, direction_new, cost_new))
            cost_board[i_new][j_new][direction_new] = cost_new

    return min(filter(lambda x: x != -1, cost_board[len_board - 1][len_board - 1]))


print(solution(board0))
print(solution(board1))
print(solution(board2))
print(solution(board3))
