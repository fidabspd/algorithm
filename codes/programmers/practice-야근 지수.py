# https://school.programmers.co.kr/learn/courses/30/lessons/12927
works0 = [4, 3, 3]
n0 = 4  # 12
works1 = [2, 1, 2]
n1 = 1  # 6
works2 = [1, 1]
n2 = 3  # 0


def solution(n, works):
    import heapq

    if sum(works) <= n:
        return 0

    works = [-_ for _ in works]
    heapq.heapify(works)
    for _ in range(n):
        now = heapq.heappop(works)
        now += 1
        heapq.heappush(works, now)

    return sum([(-_) ** 2 for _ in works])


print(solution(n0, works0))
print(solution(n1, works1))
print(solution(n2, works2))
