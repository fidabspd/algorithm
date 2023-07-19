# https://school.programmers.co.kr/learn/courses/30/lessons/132265
topping0 = [1, 2, 1, 3, 1, 4, 1, 2]  # 2
topping1 = [1, 2, 3, 1, 4]  # 0


def solution(topping):
    from collections import Counter, defaultdict

    answer = 0
    a, b = defaultdict(int), Counter(topping)
    len_a, len_b = 0, len(b)
    for t in topping:
        a[t] += 1
        b[t] -= 1
        if a[t] == 1:
            len_a += 1
        if b[t] == 0:
            del b[t]
            len_b -= 1
        if len_a == len_b:
            answer += 1
    return answer


print(solution(topping0))
print(solution(topping1))
