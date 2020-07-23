numbers = [1, 1, 1, 1, 1]; target = 3;  # 5

def solution(numbers, target):
    answer = [0]
    for num in numbers:
        tmp = []
        for ans in answer:
            tmp.append(ans + num)
            tmp.append(ans - num)
        answer = tmp

    return answer.count(target)

print(solution(numbers, target))


### 다른 사람의 풀이
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
        