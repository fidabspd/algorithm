n = 5; results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]  # 2


def solution(n, results):
    from collections import deque
    
    def get_graph():
        graph = {i: {'win': set(), 'lose': set()} for i in range(1, n+1)}
        for w, l in results:
            graph[w]['win'].add(l)
            graph[l]['lose'].add(w)
        return graph
    
    graph = get_graph()
    
    def update_graph(node, wol):
        q = deque(graph[node][wol])
        visited = [False]*n
        while q:
            now = q.pop()
            if visited[now-1]:
                continue
            visited[now-1] = True
            graph[node][wol].update(graph[now][wol])
            q.extend(graph[now][wol])
            
    for i in range(n):
        for wol in ['win', 'lose']:
            update_graph(i+1, wol)
        
    fixed = [k for k in graph.keys()
             if len(graph[k]['win'])+len(graph[k]['lose']) == n-1]
    
    return len(fixed)


print(solution(n, results))
