array = [1, 5, 2, 6, 3, 7, 4]
command = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# return [5, 6, 3]


### 통과
def solution(array, commands):
    import heapq as hq
    answer = []
    for com in commands:
        arr = array[com[0]-1:com[1]]
        for idx in range(com[2]):
            hq.heapify(arr)
            tmp = hq.heappop(arr)
        answer.append(tmp)
    return answer

print(solution(array, command))