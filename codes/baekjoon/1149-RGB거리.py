import sys

n = int(sys.stdin.readline())
costs = []
for _ in range(n):
    costs.append(list(map(int, sys.stdin.readline().split(' '))))


def solution(n, costs):
    copied = costs[:]
    for i in range(1, n):
        copied[i][0] += min(copied[i-1][1], copied[i-1][2])
        copied[i][1] += min(copied[i-1][0], copied[i-1][2])
        copied[i][2] += min(copied[i-1][0], copied[i-1][1])
    return min(copied[-1])


print(solution(n, costs))
