# https://school.programmers.co.kr/learn/courses/30/lessons/172927
picks0 = [1, 3, 2]
minerals0 = [
    "diamond",
    "diamond",
    "diamond",
    "iron",
    "iron",
    "diamond",
    "iron",
    "stone",
]  # 12
picks1 = [0, 1, 1]
minerals1 = [
    "diamond",
    "diamond",
    "diamond",
    "diamond",
    "diamond",
    "iron",
    "iron",
    "iron",
    "iron",
    "iron",
    "diamond",
]  # 50


def solution(picks, minerals):
    answer = 0
    minerals = minerals[: sum(picks) * 5]
    tmps = []
    tmp = [0, 0, 0]
    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            tmp[0] += 1
            tmp[1] += 5
            tmp[2] += 25
        elif minerals[i] == "iron":
            tmp[0] += 1
            tmp[1] += 1
            tmp[2] += 5
        elif minerals[i] == "stone":
            tmp[0] += 1
            tmp[1] += 1
            tmp[2] += 1

        if (i + 1) % 5 == 0 or i == len(minerals) - 1:
            tmps.append(tmp)
            tmp = [0, 0, 0]

    tmps.sort(key=lambda x: (-x[2], -x[1], x[0]))
    is_sorted = False
    for i in range(len(tmps)):
        tmp = tmps.pop(0)
        if picks[0] != 0:
            picks[0] -= 1
            answer += tmp[0]
        elif picks[1] != 0:
            if not is_sorted:
                is_sorted = True
                tmps.sort(key=lambda x: (-x[2], x[1]))
            picks[1] -= 1
            answer += tmp[1]
        elif picks[2] != 0:
            picks[2] -= 1
            answer += tmp[2]

    return answer


print(solution(picks0, minerals0))
print(solution(picks1, minerals1))
