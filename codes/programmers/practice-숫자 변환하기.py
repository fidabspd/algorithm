# https://school.programmers.co.kr/learn/courses/30/lessons/154538
x0 = 10
y0 = 40
n0 = 5  # 2
x1 = 10
y1 = 40
n1 = 30  # 1
x2 = 2
y2 = 5
n2 = 4  # -1


def solution_timeout(x, y, n):
    from collections import deque

    if x == y:
        return 0

    queue = deque([[x, 0]])
    while queue:
        out, t = queue.popleft()
        xn = out + n
        x2 = out * 2
        x3 = out * 3
        if xn < y:
            queue.append([xn, t + 1])
        elif xn == y:
            return t + 1
        if x2 < y:
            queue.append([x2, t + 1])
        elif x2 == y:
            return t + 1
        if x3 < y:
            queue.append([x3, t + 1])
        elif x3 == y:
            return t + 1
    return -1


def solution(x, y, n):
    from collections import deque

    queue = deque([[y, 0]])
    while queue:
        out, t = queue.popleft()
        if out == x:
            return t
        elif out < x:
            continue

        queue.append([out - n, t + 1])
        if out % 2 == 0:
            queue.append([out // 2, t + 1])
        if out % 3 == 0:
            queue.append([out // 3, t + 1])

    return -1


print(solution(x0, y0, n0))
print(solution(x1, y1, n1))
print(solution(x2, y2, n2))
