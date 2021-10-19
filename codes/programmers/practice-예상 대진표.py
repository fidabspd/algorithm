N = 8; A = 4; B = 7;  # 3


def solution(N, A, B):
    A = A-1
    B = B-1
    answer = 0

    while A != B:
        A //= 2
        B //= 2
        answer += 1

    return answer


print(solution(N, A, B))
