n1 = 9; wires1 = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]  # 3
n2 = 4; wires2 = [[1,2],[2,3],[3,4]]  # 0
n3 = 7; wires3 = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]  # 1


def solution(n, wires):
    min_diff = len(wires)
    for d in range(len(wires)):
        wires_del = wires[:d] + wires[d+1:]
        connection1 = wires_del[0].copy()
        connection2 = []
        for i, j in wires_del[1:]:
            if i in connection1 or j in connection1:
                if i in connection1 and j not in connection1:
                    connection1.append(j)
                elif j in connection1 and i not in connection1:
                    connection1.append(i)
            else:
                if not connection2:
                    connection2 = [i, j]
                elif i in connection2 and j not in connection2:
                    connection2.append(j)
                elif j in connection2 and i not in connection2:
                    connection2.append(i)
        diff = abs(len(connection1) - len(connection2))
        if min_diff > diff:
            min_diff = diff
    return min_diff


print(solution(n1, wires1))
print(solution(n2, wires2))
print(solution(n3, wires3))
