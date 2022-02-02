n1 = 9; wires1 = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]  # 3
n2 = 4; wires2 = [[1,2],[2,3],[3,4]]  # 0
n3 = 7; wires3 = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]  # 1


def solution(n, wires):
    from collections import deque
    min_diff = n
    for j in range(len(wires)):
        del_wires = wires.copy()
        d = del_wires[j].copy()
        del del_wires[j]
        
        queue = deque([d[0]])
        visited = [False for _ in range(len(del_wires))]
        l = 1
        while queue:
            now = queue.popleft()
            for i in range(len(del_wires)):
                if now in del_wires[i] and not visited[i]:
                    visited[i] = True
                    for w in del_wires[i]:
                        if w != now:
                            queue.append(w)
                            l += 1
        diff = abs((n - l) - l)
        if diff < min_diff:
            min_diff = diff
    return min_diff


print(solution(n1, wires1))
print(solution(n2, wires2))
print(solution(n3, wires3))
