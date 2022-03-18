import sys
from collections import deque

v = int(sys.stdin.readline())
graph = {i+1:[] for i in range(v)}
for _ in range(v):
    tmp = list(map(int, sys.stdin.readline().split(' ')))
    s = tmp[0]
    for e, d in zip(tmp[1:-1:2], tmp[2:-1:2]):
        graph[s].append([e, d])

def get_dist(start):
    dist = [0]*v
    visited = [False]*v
    queue = deque([start])
    while queue:
        now = queue.popleft()
        visited[now-1] = True
        for e, d in graph[now]:
            if visited[e-1]:
                continue
            visited[e-1] = True
            queue.append(e)
            dist[e-1] = dist[now-1]+d
    return dist

dist = get_dist(1)
max_idx = dist.index(max(dist))+1
print(max(get_dist(max_idx)))
