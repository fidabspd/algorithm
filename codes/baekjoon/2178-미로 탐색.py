import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split(' '))
path = []
for _ in range(n):
    path.append(list(map(int, list(sys.stdin.readline())[:-1])))


def solution(n, m, path):
    q = deque([[0, 0]])
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while q:
        now = q.popleft()
        i, j = now
        for x, y in move:
            new_i, new_j = i+x, j+y
            if not (0 <= new_i < n and 0<= new_j < m):
                continue
            if path[new_i][new_j] != 1 or (new_i, new_j) == (0, 0):
                continue
            q.append([new_i, new_j])
            path[new_i][new_j] += path[i][j]
    return path[-1][-1]


print(solution(n, m, path))
