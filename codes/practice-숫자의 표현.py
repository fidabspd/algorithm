n = 15  # 4


def solution(n):
    check = 1
    answer = 0
    for i in range(2, n):
        if check >= n:
            break
        if i%2 == 0:
            if (n/i)-(n//i) == 0.5:
                answer += 1
        else:
            if n%i == 0:
                answer += 1
        check += i
    return answer+1


print(solution(n))
