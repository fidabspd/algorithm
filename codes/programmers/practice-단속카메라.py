routes0 = [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]  # 2


def solution(routes):
    routes.sort()
    old_e = -30001
    answer = 0
    for s, e in routes:
        if s > old_e:
            answer += 1
            old_e = e
        if e < old_e:
            old_e = e
    return answer


print(solution(routes0))
