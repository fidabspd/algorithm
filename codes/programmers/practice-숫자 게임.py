A0 = [5, 1, 3, 7]
B0 = [2, 2, 6, 8]  # 3
A1 = [2, 2, 2, 2]
B1 = [1, 1, 1, 1]  # 0


def solution(A, B):
    import heapq

    A = [-_ for _ in A + [0]]
    B = [-_ for _ in B + [0]]
    heapq.heapify(A)
    heapq.heapify(B)

    answer = 0
    now_A = -heapq.heappop(A)
    now_B = -heapq.heappop(B)
    while now_A and now_B:
        if now_A >= now_B:
            now_A = -heapq.heappop(A)
            continue
        answer += 1
        now_A = -heapq.heappop(A)
        now_B = -heapq.heappop(B)

    return answer


print(solution(A0, B0))
print(solution(A1, B1))
