n0 = 7
k0 = 3
enemy0 = [4, 2, 4, 5, 3, 3, 1]  # 5
n1 = 2
k1 = 4
enemy1 = [3, 3, 3, 3]  # 4


def solution(n, k, enemy):
    import heapq

    coupon = enemy[:k]
    heapq.heapify(coupon)
    answer = len(coupon)

    for now in enemy[k:]:
        if now > coupon[0]:
            heapq.heappush(coupon, now)
            now = heapq.heappop(coupon)
        if now > n:
            break
        n -= now
        answer += 1
    return answer


print(solution(n0, k0, enemy0))
print(solution(n1, k1, enemy1))
