maps1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]  # 11
maps2 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]  # -1


def solution(maps):
    from collections import deque
    
    graph = maps.copy()
    
    n = len(graph)
    m = len(graph[0])
    
    if (n, m) == (1, 1):
        return 1
    
    queue = deque()
    queue.append((0, 0))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or (nx, ny) == (0, 0):
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
            
    return graph[n-1][m-1] if graph[n-1][m-1] not in (0, 1) else -1


print(solution(maps1))
print(solution(maps2))
