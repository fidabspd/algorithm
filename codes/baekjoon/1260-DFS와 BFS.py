n1 = 4; m1 = 5; v1 = 1; edge_info1 = [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]]
n2 = 5; m2 = 5; v2 = 3; edge_info2 = [[5, 4], [5, 2], [1, 2], [3, 4], [3, 1]]
n3 = 1000; m3 = 1; v3 = 1000; edge_info3 = [[999, 1000]]


from collections import deque

def make_graph(edge_info):
    graph = {}
    for n1, n2 in edge_info:
        if n1 not in graph.keys():
            graph[n1] = [n2]
        elif n2 not in graph[n1]:
            graph[n1].append(n2)
        if n2 not in graph.keys():
            graph[n2] = [n1]
        elif n1 not in graph[n2]:
            graph[n2].append(n1)
    return graph

def dfs(graph, v):
    visited = []
    stack = [v]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                tmp = list(set(graph[n]) - set(visited))
                tmp.sort(reverse=True)  # stack이기 때문에 처음이 마지막으로 오도록.
                stack += tmp
    return visited

def bfs(graph, v):
    visited = []
    queue = deque([v])
    
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph.keys():
                tmp = list(set(graph[n]) - set(visited))
                tmp.sort()
                queue += tmp
    return visited

def solution(n, m, v, edge_info):
    graph = make_graph(edge_info)
    return dfs(graph, v), bfs(graph, v)


print(solution(n1, m1, v1, edge_info1))
print(solution(n2, m2, v2, edge_info2))
print(solution(n3, m3, v3, edge_info3))
