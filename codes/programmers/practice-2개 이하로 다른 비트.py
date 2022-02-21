numbers = [2,7]  # [3,11]


def solution(numbers):
    answer = []
    for num in numbers:
        num = list(bin(int(num))[2:])
        num = num[::-1]
        for i, n in enumerate(num):
            if n == '0':
                num[i] = '1'
                if i != 0:
                    num[i-1] = '0'
                break
        else:
            num[-1] = '0'
            num.append('1')
        num = num[::-1]
        num = int(''.join(num), 2)
        answer.append(num)
    return answer


print(solution(numbers))


def solution_else(numbers):
    answer = []
    for num in numbers:
        answer.append(((num^(num+1)) >> 2) + num+1)
    return answer
    