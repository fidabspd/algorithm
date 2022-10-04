n = 2  # [[1, 2], [1, 3], [2, 3]]
n = 3  # [[1, 3], [1, 2], [3, 2], [1, 3], [2, 1], [2, 3], [1, 3]]
n = 4  # [[1, 2], [1, 3], [2, 3], [1, 2], [3, 1], [3, 2], [1, 2], [1, 3], [2, 3], [2, 1], [3, 1], [2, 3], [1, 2], [1, 3], [2, 3]]


def move_tower(n, now, target):
    if n == 1:
        return [[now, target]]

    for i in [1, 2, 3]:
        if i not in [now, target]:
            remain = i

    return move_tower(n - 1, now, remain) + [[now, target]] + move_tower(n - 1, remain, target)


def solution(n):
    return move_tower(n, 1, 3)


print(solution(2))
print(solution(3))
print(solution(4))
