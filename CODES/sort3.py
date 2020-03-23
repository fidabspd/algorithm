citations = [3, 0, 6, 1, 5]  # return 3

### 알고리즘 틀림
def solution1(citations):
    import heapq as hq
    hq.heapify(citations)
    answer = 0
    for i in range(len(citations)):
        if citations[0] >= len(citations):
            answer = citations[0]
            break
        else:
            hq.heappop(citations)
    return answer

#print(solution1(citations))



### 문제를 잘못이해함.
def solution2(citations):
    import heapq as hq
    citations = [-c for c in citations]
    hq.heapify(citations)
    cnt = 1
    for i in range(len(citations)):
        print(citations)
        if -citations[0] > cnt:
            hq.heappop(citations)
            cnt += 1
        else:
            return -citations[0]

#print(solution2(citations))



### 통과
def solution(citations):
    import heapq as hq
    citations = [-c for c in citations]
    hq.heapify(citations)
    tmp = []
    answer = 0
    for i in range(len(citations)):
        hq.heappush(tmp, (-hq.heappop(citations)))
        print(citations, tmp)
        answer = max(answer, min(len(tmp), tmp[0]))
    return answer

print(solution(citations))
print(solution([7,7,7]))
print(solution([7,7,7,7,2,2]))