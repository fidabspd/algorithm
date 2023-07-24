# https://school.programmers.co.kr/learn/courses/30/lessons/140107
k0 = 2
d0 = 4  # 6
k1 = 1
d1 = 5  # 26


def solution(k, d):
    answer = 0
    x = d - (d % k)
    y = 0
    while x >= 0:
        if x**2 + y**2 <= d**2:
            answer += x // k + 1
            y += k
        else:
            x -= k
    return answer


print(solution(k0, d0))
print(solution(k1, d1))


def solution_else(k, d):
    c = 0
    for y in range(0, d, k):
        x = (d**2 - y**2) ** 0.5
        c += x // k
    return c + d // k + 1
