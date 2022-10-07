n = 3
k = 5
# [3,1,2]


def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n


def solution(n, k):
    answer = []
    k -= 1
    _list = list(range(1, n + 1))
    for i in range(n - 1, 0, -1):
        pick, k = divmod(k, factorial(i))
        answer.append(_list.pop(pick))
    return answer + _list


print(solution(n, k))
