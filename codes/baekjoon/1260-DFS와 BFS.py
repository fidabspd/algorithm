n1 = 4; m1 = 5; v1 = 1; edge_info1 = [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]]
n2 = 5; m2 = 5; v2 = 3; edge_info2 = [[5, 4], [5, 2], [1, 2], [3, 4], [3, 1]]
n3 = 1000; m3 = 1; v3 = 1000; edge_info3 = [[999, 1000]]


from collections import deque

def get_graph(n, edges):
    graph = {i+1: [] for i in range(n)}
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)
    return graph

def dfs(graph, v):
    visited = []
    stack = [v]
    while stack:
        now = stack.pop()
        if now in visited:
            continue
        visited.append(now)
        stack.extend(sorted(graph[now], reverse=True))
    return visited

def bfs(graph, v):
    from collections import deque

    visited = []
    queue = deque([v])
    while queue:
        now = queue.popleft()
        if now in visited:
            continue
        visited.append(now)
        queue.extend(sorted(graph[now]))

    return visited

def solution(n, m, v, edges):
    graph = get_graph(n, edges)
    return dfs(graph, v), bfs(graph, v)


print(solution(n1, m1, v1, edge_info1))
print(solution(n2, m2, v2, edge_info2))
print(solution(n3, m3, v3, edge_info3))
