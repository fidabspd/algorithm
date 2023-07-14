# https://school.programmers.co.kr/learn/courses/30/lessons/154540
maps0 = ["X591X", "X1X5X", "X231X", "1XXX1"]  # [1, 1, 27]
maps1 = ["XXX", "XXX", "XXX"]  # [-1]


def solution(maps):
    from collections import deque

    def check_valid_index(i, j):
        if -1 < i < height and -1 < j < width:
            return True
        return False

    def get_sum(i, j):
        _sum = 0
        queue = deque([[i, j]])
        checked[i][j] = 1
        while queue:
            i, j = queue.popleft()
            if maps[i][j] == "X":
                continue
            _sum += int(maps[i][j])
            if check_valid_index(i - 1, j) and checked[i - 1][j] == 0:
                queue.append([i - 1, j])
                checked[i - 1][j] = 1
            if check_valid_index(i + 1, j) and checked[i + 1][j] == 0:
                queue.append([i + 1, j])
                checked[i + 1][j] = 1
            if check_valid_index(i, j - 1) and checked[i][j - 1] == 0:
                queue.append([i, j - 1])
                checked[i][j - 1] = 1
            if check_valid_index(i, j + 1) and checked[i][j + 1] == 0:
                queue.append([i, j + 1])
                checked[i][j + 1] = 1
        return _sum

    answer = []
    width, height = len(maps[0]), len(maps)
    checked = [[0] * width for _ in range(height)]
    for i in range(height):
        for j in range(width):
            if checked[i][j] == 1:
                continue
            _sum = get_sum(i, j)
            if _sum:
                answer.append(_sum)
    if answer:
        return sorted(answer)
    else:
        return [-1]


print(solution(maps0))
print(solution(maps1))
