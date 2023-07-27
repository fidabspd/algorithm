# https://school.programmers.co.kr/learn/courses/30/lessons/148653
storey0 = 16  # 6
storey1 = 2554  # 16


def solution(storey):
    answer = 0
    i = -1
    while storey:
        str_storey = str(storey)
        now = int(str_storey[i])
        if now < 5:
            answer += now
            storey -= now * 10 ** (-i - 1)
        elif now > 5:
            answer += 10 - now
            storey += (10 - now) * 10 ** (-i - 1)
        elif -i == len(str_storey):
            answer += now
            storey -= now * 10 ** (-i - 1)
        elif int(str_storey[i - 1]) >= 5:
            answer += 10 - now
            storey += (10 - now) * 10 ** (-i - 1)
        elif int(str_storey[i - 1]) < 5:
            answer += now
            storey -= now * 10 ** (-i - 1)
        else:
            raise Exception
        i -= 1

    return answer


print(solution(storey0))
print(solution(storey1))
print(solution(555))


def solution(storey):
    if storey < 10:
        return min(storey, 11 - storey)
    left = storey % 10
    return min(left + solution(storey // 10), 10 - left + solution(storey // 10 + 1))
