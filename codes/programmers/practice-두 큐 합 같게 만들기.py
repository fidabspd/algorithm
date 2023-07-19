# https://school.programmers.co.kr/learn/courses/30/lessons/118667
queue10 = [3, 2, 7, 2]
queue20 = [4, 6, 5, 1]  # 2
queue11 = [1, 2, 1, 2]
queue21 = [1, 10, 1, 2]  # 7
queue12 = [1, 1]
queue22 = [1, 5]  # -1


def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total = sum1 + sum2
    if total % 2 != 0:
        return -1

    obj = total // 2
    queue = queue1 + queue2 + queue1
    start = 0
    end = len(queue1)

    answer = 0
    while end < len(queue):
        if sum1 == obj:
            return answer
        elif sum1 < obj:
            sum1 += queue[end]
            end += 1
            answer += 1
        elif sum1 > obj:
            sum1 -= queue[start]
            start += 1
            answer += 1

    return -1


print(solution(queue10, queue20))
print(solution(queue11, queue21))
print(solution(queue12, queue22))
