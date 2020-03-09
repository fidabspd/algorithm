scoville = [1, 2, 3, 9, 10, 12]
K = 7
# return 2


### 시간초과
def solution1(scoville, K):
    scoville.sort()
    for i in range(len(scoville) - 1):
        print(scoville)
        m1 = scoville.pop(0)
        m2 = scoville.pop(0)
        scoville.append(m1 + m2 * 2)
        scoville.sort()
        if scoville[0] >= K:
            break
    if scoville[0] < K:
        return -1
    else:
        return i + 1

# print(solution1(scoville, K))


### heap 이용
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    for i in range(len(scoville) - 1):
        m1 = heapq.heappop(scoville)
        m2 = heapq.heappop(scoville)
        heapq.heappush(scoville, m1 + m2 * 2)
        if scoville[0] >= K:
            break
    if scoville[0] < K:
        return -1
    else:
        return i + 1

print(solution(scoville, K))
