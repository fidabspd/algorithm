N1 = 5; road1 = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]; K1 = 3  # 4
N2 = 6; road2 = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]; K2 = 4  # 4


def solution(N, road, K):
    from collections import deque
    import math
    
    dist = {i+1:math.inf for i in range(N)}
    dist[1] = 0
    graph = {i+1:[] for i in range(N)}
    for s, e, t in road:
        graph[s].append((s, e, t))
        graph[e].append((e, s, t))
    for i in range(N):
        graph[i+1].sort()
    
    queue = deque(graph[1])
    while queue:
        s, e, t = queue.popleft()
        if dist[e] < dist[s]+t:
            continue
        queue.extend(graph[e])
        dist[e] = dist[s]+t
    
    return sum([0 if dist[i+1]>K else 1 for i in range(N)])
    

print(solution(N1, road1, K1))
print(solution(N2, road2, K2))
