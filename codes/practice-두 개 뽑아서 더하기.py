numbers1 = [2,1,3,4,1]  # [2,3,4,5,6,7]
numbers2 = [5,0,2,7]  # [2,5,7,9,12]

def solution(numbers):
    answer = []
    while numbers:
        now = numbers[0]
        numbers = numbers[1:]
        for i in numbers:
            answer.append(now+i)

    answer = list(set(answer))
    answer.sort()
    return answer

print(solution(numbers1))
print(solution(numbers2))
