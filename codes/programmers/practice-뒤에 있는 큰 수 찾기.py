# https://school.programmers.co.kr/learn/courses/30/lessons/154539
numbers0 = [2, 3, 3, 5]  # [3, 5, 5, -1]
numbers1 = [9, 1, 5, 3, 6, 2]  # [-1, 5, 6, 6, -1, -1]


def solution_timeout(numbers):
    len_numbers = len(numbers)
    answer = [-1] * len_numbers
    not_founded = [0]
    for i in range(1, len_numbers):
        j = 0
        while j < len(not_founded):
            if numbers[not_founded[j]] < numbers[i]:
                answer[not_founded[j]] = numbers[i]
                not_founded = not_founded[:j] + not_founded[j + 1 :]
            else:
                j += 1
        not_founded.append(i)

    return answer


def solution(numbers):
    len_numbers = len(numbers)
    answer = [-1] * len_numbers
    stack = [[0, numbers[0]]]
    for i in range(1, len_numbers):
        now_num = numbers[i]
        while stack and stack[-1][1] < now_num:
            answer[stack[-1][0]] = now_num
            stack.pop()
        stack.append([i, now_num])
    return answer


print(solution(numbers0))
print(solution(numbers1))
