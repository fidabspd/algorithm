N1 = 5  # 2
N2 = 6  # 2
N3 = 5000  # 5


def solution(N):
    answer = 0
    while N != 0:
        if N%2 != 0:
            answer += 1
        N //= 2
    return answer


print(solution(N1))
print(solution(N2))
print(solution(N3))
