# https://school.programmers.co.kr/learn/courses/30/lessons/159993
maps0 = [
    "SOOOL",
    "XXXXO",
    "OOOOO",
    "OXXXX",
    "OOOOE",
]  # 16
maps1 = [
    "LOOXS",
    "OOOOX",
    "OOOOO",
    "OOOOO",
    "EOOOO",
]  # -1


def solution(maps):
    from collections import deque

    def check_point(i, j, dist):
        if not (0 <= i < n_rows and 0 <= j < n_cols):
            return False
        elif maps[i][j] == "X":
            return False
        elif dist[i][j]:
            return False
        else:
            return True

    def find_path(start, end):
        dist = [[0] * n_cols for _ in range(n_rows)]
        queue = deque([start])
        while queue:
            i, j = queue.popleft()
            if [i, j] == end:
                return dist[i][j]
            if check_point(i + 1, j, dist):
                dist[i + 1][j] = dist[i][j] + 1
                queue.append([i + 1, j])
            if check_point(i - 1, j, dist):
                dist[i - 1][j] = dist[i][j] + 1
                queue.append([i - 1, j])
            if check_point(i, j + 1, dist):
                dist[i][j + 1] = dist[i][j] + 1
                queue.append([i, j + 1])
            if check_point(i, j - 1, dist):
                dist[i][j - 1] = dist[i][j] + 1
                queue.append([i, j - 1])
        return -1

    n_rows = len(maps)
    n_cols = len(maps[0])
    for i in range(n_rows):
        for j in range(n_cols):
            if maps[i][j] == "S":
                s_point = [i, j]
            elif maps[i][j] == "E":
                e_point = [i, j]
            elif maps[i][j] == "L":
                l_point = [i, j]

    s_to_l = find_path(s_point, l_point)
    if s_to_l == -1:
        return -1
    l_to_e = find_path(l_point, e_point)
    if l_to_e == -1:
        return -1

    return s_to_l + l_to_e


print(solution(maps0))
print(solution(maps1))
