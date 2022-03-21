n1 = 6; s1 = 4; a1 = 6; b1 = 2
fares1 = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]  # 82
n2 = 7; s2 = 3; a2 = 4; b2 = 1
fares2 = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]  # 14
n3 = 6; s3 = 4; a3 = 5; b3 = 6
fares3 = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]  # 18


def solution(n, s, a, b, fares):
    
    def get_graph():
        graph = [[] for _ in range(n)]
        for c, d, f in fares:
            graph[c-1].append([d, f])
            graph[d-1].append([c, f])
        return graph
    graph = get_graph()
    
    def get_min_fares(fr):
        visited = [False]*n
        min_fares = [float('inf')]*n
        min_fares[fr-1] = 0; visited[fr-1] = True
        
        def update_min_fare(base):
            for d, f in graph[base-1]:
                min_fares[d-1] = min(min_fares[d-1], min_fares[base-1]+f)
                
        def get_min_node():
            tmp = [float('inf') if v else f for f, v in zip(min_fares, visited)]
            return tmp.index(min(tmp))+1
        
        update_min_fare(fr)
        before_min_node = -1
        while sum(visited) != len(visited):
            min_node = get_min_node()
            if before_min_node == min_node:
                break
            update_min_fare(min_node)
            visited[min_node-1] = True
            before_min_node = min_node
            
        return min_fares
        
    fares_s = get_min_fares(s)
    fares_a = get_min_fares(a)
    fares_b = get_min_fares(b)
    
    answer = float('inf')
    for f in zip(fares_s, fares_a, fares_b):
        if sum(f) < answer:
            answer = sum(f)
        
    return answer


print(solution(n1, s1, a1, b1, fares1))
print(solution(n2, s2, a2, b2, fares2))
print(solution(n3, s3, a3, b3, fares3))


def solution_with_heapq(n, s, a, b, fares):
    import heapq
    
    graph = [[] for _ in range(n+1)]
    for c, d, f in fares:
        graph[c].append([d, f])
        graph[d].append([c, f])
    
    def get_min_dist(start):
        distances = [float('inf')]*(n+1)
        distances[start] = 0
        q = [(0, start)]
        while q:
            dist, now = heapq.heappop(q)
            for br, d in graph[now]:
                new_dist = dist+d
                if distances[br] > new_dist:
                    distances[br] = new_dist
                    heapq.heappush(q, (new_dist, br))
        return distances
    
    s_f = get_min_dist(s)
    a_f = get_min_dist(a)
    b_f = get_min_dist(b)
    
    answer = float('inf')
    for i in range(1, n+1):
        sum_f = sum([s_f[i], a_f[i], b_f[i]])
        if sum_f < answer:
            answer = sum_f
    
    return answer
