jobs = [[0, 3], [1, 9], [2, 6]]
# return 9

### 요청이 들어오는 시간 기준으로 정렬을 한다. -> 그냥 heapify하면 됨
#   jobs[0][0] <= time 조건으로 모두 heappop하고 모두 on_disk에 heappush
#       들어올때 time - job[0][0]을 total에 더한다
#   on_disk를 완료시간이 가장 가까운 순으로 정렬한다. -> heappush하면 자동으로 됨
#   처리할 디스크가 없으면 time에 1씩 더한다 len(on_disk)가 0이면
#   len(on_disk) > 0 이면 on_disk에서 heappop하고 해당 디스크 소요시간 * len(on_disk)를 total에 더한다
#   total을 처음 len(jobs)로 나눠서 return



import heapq as hq

def solution(jobs):
    n = len(jobs)
    hq.heapify(jobs)
    time = 0
    on_disk = []
    total = 0

    while True:
        if len(jobs) > 0:
            while jobs[0][0] <= time:
                tmp = hq.heappop(jobs)
                total += time - tmp[0]
                hq.heappush(on_disk, tmp[1])
                if len(jobs) == 0:
                    break
        
        if len(on_disk) == 0:
            time = jobs[0][0]
            
        else:
            tmp = hq.heappop(on_disk)
            total += tmp * (len(on_disk) + 1)
            time += tmp
        
        if len(jobs) == 0 and len(on_disk) == 0:
            break

    # print(total)

    return int(total / n)

print((solution(jobs)))
print((solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]])))  # return 74