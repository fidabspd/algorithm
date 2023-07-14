# https://school.programmers.co.kr/learn/courses/30/lessons/138476
k0 = 6
tangerine0 = [1, 3, 2, 5, 4, 5, 2, 3]  # 3
k1 = 4
tangerine1 = [1, 3, 2, 5, 4, 5, 2, 3]  # 2
k2 = 2
tangerine2 = [1, 1, 1, 1, 2, 2, 2, 3]  # 1


def solution(k, tangerine):
    from collections import defaultdict, deque

    answer = 0

    count_dict = defaultdict(int)
    for kilo in tangerine:
        count_dict[kilo] += 1

    count_queue = deque(sorted([[k, n] for k, n in count_dict.items()], key=lambda x: x[1], reverse=True))
    count = 0
    while count < k:
        kilo, n = count_queue.popleft()
        count += n
        answer += 1

    return answer


print(solution(k0, tangerine0))
print(solution(k1, tangerine1))
print(solution(k2, tangerine2))


def solution_else(k, tangerine):
    import collections

    answer = 0
    cnt = collections.Counter(tangerine)

    for v in sorted(cnt.values(), reverse=True):
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer
