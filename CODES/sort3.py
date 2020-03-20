citations = [3, 0, 6, 1, 5]  # return 3

def solution(citations):
    import heapq as hq
    hq.heapify(citations)
    answer = 0
    for i in range(len(citations)):
        tmp = citations
        if citations[0] >= len(citations):
            answer = citations[0]
            break
        else:
            hq.heappop(citations)
    return answer

print(solution(citations))