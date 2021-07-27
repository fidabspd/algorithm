n1 = 45  # 7
n2 = 125  # 229


def solution(n):
    transform = ''
    i = 1
    while n > 0:
        transform = str(n%3) + transform
        n //= 3

    i_3 = 1
    answer = 0
    for i in transform:
        answer += int(i) * i_3
        i_3 *= 3
    
    return answer


print(solution(n1))
print(solution(n2))
