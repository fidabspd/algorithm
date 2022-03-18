n, k = map(int, input().split(' '))
edges = []
for _ in range(k):
    edges.append(list(map(int, input().split(' '))))


def get_graph(n, edges):
    graph = {i+1: [] for i in range(n)}
    for s, e, d in edges:
        graph[s].append([e, d])
    return graph

def solution(n, edges):
    
    graph = get_graph(n, edges)
    distances = {i+1: 0 if i==0 else float('inf') for i in range(n)}
    visited = [False]*n

    def update_dist(start):
        for e, d in graph[start]:
            if distances[e] > distances[start]+d:
                distances[e] = distances[start]+d

    def get_min_dist_node():
        dist = float('inf')
        node = None
        for i in range(n):
            if not visited[i] and distances[i+1]<dist:
                dist = distances[i+1]
                node = i+1
        return node

    while sum(visited) != len(visited):
        now = get_min_dist_node()
        update_dist(now)
        visited[now-1] = True
        print(distances, visited)

    return distances


print(solution(n, edges))


# input:
# 6 11
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
# result: {1: 0, 2: 2, 3: 3, 4: 1, 5: 2, 6: 4}