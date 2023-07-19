# https://school.programmers.co.kr/learn/courses/30/lessons/131704
order0 = [4, 3, 1, 2, 5]  # 2
order1 = [5, 4, 3, 2, 1]  # 5


def solution(order):
    from collections import deque

    answer = 0
    stack = []
    queue = deque([_ for _ in range(1, len(order) + 1)])
    while True:
        if queue and queue[0] == order[answer]:
            queue.popleft()
            answer += 1
        elif stack and stack[-1] == order[answer]:
            stack.pop()
            answer += 1
        else:
            stack.append(queue.popleft())
        if not queue and (answer == len(order) or stack[-1] != order[answer]):
            break

    return answer


print(solution(order0))
print(solution(order1))
