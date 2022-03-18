t = int(input())
ns, dss, rules, ws = [], [], [], []
for _ in range(t):
    n, k = list(map(int, input().split(' ')))
    ds = list(map(int, input().split(' ')))
    rule = []
    for _ in range(k):
        rule.append(list(map(int, input().split(' '))))
    w = int(input())
    ns.append(n)
    dss.append(ds)
    rules.append(rule)
    ws.append(w)


def get_graph(n, rule):
    graph = {i+1: [] for i in range(n)}
    in_degree = [0]*n
    for x, y in rule:
        graph[x].append(y)
        in_degree[y-1] += 1
    return graph, in_degree

def solution(n, rule, w, ds):
    from collections import deque

    times = ds[:]
    graph, in_degree = get_graph(n, rule)

    can_start = [i+1 for i in range(n) if in_degree[i]==0]
    queue = deque(can_start)
    while queue:
        now = queue.popleft()
        print(in_degree)
        for n in graph[now]:
            in_degree[n-1] -= 1
            if not in_degree[n-1]:
                queue.append(n)
            times[n-1] = max(times[now-1]+ds[n-1], times[n-1])
    
    return times[w-1]
        

for n, rule, w, ds in zip(ns, rules, ws, dss):
    print(solution(n, rule, w, ds))
