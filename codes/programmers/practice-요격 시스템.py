targets = [[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]  # 3


def solution(targets):
    targets.sort(reverse=True)
    s, e = 100000000, 0
    answer = 0
    while targets:
        new_s, new_e = targets.pop()
        s = max(s, new_s)
        e = min(e, new_e)
        if not s < e:
            s, e = new_s, new_e
            answer += 1
    return answer


print(solution(targets))
