board0 = [
    "...D..R",
    ".D.G...",
    "....D.D",
    "D....D.",
    "..D....",
]  # 7
board1 = [
    ".D.R",
    "....",
    ".G..",
    "...D",
]  # -1


def solution(board):
    from collections import deque

    def check_stop_point(x, y):
        return (not (-1 < x < width and -1 < y < height)) or board[y][x] == "D"

    height = len(board)
    width = len(board[0])
    count = [[0] * width for _ in range(height)]
    y_start = [y for y in range(height) if "R" in board[y]][0]
    x_start = [x for x in range(width) if board[y_start][x] == "R"][0]
    queue = deque([[x_start, y_start]])
    while queue:
        x_now, y_now = queue.popleft()
        for x_move, y_move in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = x_now, y_now
            while True:
                x += x_move
                y += y_move
                if check_stop_point(x, y):
                    x -= x_move
                    y -= y_move
                    break
            if board[y][x] == "G":
                return count[y_now][x_now] + 1
            elif not count[y][x] and board[y][x] != "R":
                count[y][x] = count[y_now][x_now] + 1
                queue.append([x, y])
    return -1


print(solution(board0))
print(solution(board1))
