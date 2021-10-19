A1 = [1, 4, 2]; B1 = [5, 4, 4]  # 29
A2 = [1,2]; B2 = [3,4]  # 10


def solution(A, B):
    answer = 0
    for a, b in zip(sorted(A), sorted(B, reverse=True)):
        answer += a*b
    return answer


print(solution(A1, B1))
print(solution(A2, B2))
