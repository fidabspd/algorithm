# https://school.programmers.co.kr/learn/courses/30/lessons/152996
weights = [100, 180, 360, 100, 270]  # 4


def solution_timeover(weights):
    couple = []
    for mul1, mul2 in [[1, 1], [2, 3], [2, 4], [3, 4]]:
        arr1, arr2 = [_ * mul1 for _ in weights], [_ * mul2 for _ in weights]
        for i in range(len(weights)):
            for j in range(len(weights)):
                if i != j and arr1[i] == arr2[j] and sorted([i, j]) not in couple:
                    couple.append(sorted([i, j]))
    return len(couple)


def solution(weights):
    from collections import Counter

    def check(arr1, arr2):
        nonlocal answer
        i, j = 0, 0
        while i < len(arr1):
            if i == j:
                i += 1
            elif arr1[i] == arr2[j]:
                answer += counter[weights[i]] * counter[weights[j]]
                i += 1
            elif arr1[i] < arr2[j]:
                i += 1
            elif arr1[i] > arr2[j]:
                j += 1
            else:
                raise Exception

    answer = 0
    counter = Counter(weights)
    for v in counter.values():
        if v > 1:
            answer += (v * (v - 1)) // 2

    weights = sorted(list(counter.keys()))
    for mul1, mul2 in [[2, 3], [2, 4], [3, 4]]:
        arr1, arr2 = [_ * mul1 for _ in weights], [_ * mul2 for _ in weights]
        check(arr1, arr2)

    return answer


print(solution(weights))


def solution_else(weights):
    from collections import defaultdict

    answer = 0
    info = defaultdict(int)
    for w in weights:
        answer += (
            info[w]
            + info[w * 2]
            + info[w / 2]
            + info[(w * 2) / 3]
            + info[(w * 3) / 2]
            + info[(w * 4) / 3]
            + info[(w * 3) / 4]
        )
        info[w] += 1
    return answer
