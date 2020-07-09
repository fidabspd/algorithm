operations1 = ["I 16","D 1"]  # return [0,0]
operations = ["I 7","I 5","I -5","D -1"]  #return [7,5]


### 알고리즘 틀림
def solution(operations):
    import heapq as hq
    li1 = []; li2 = []
    cnt_i = 0; cnt_d = 0

    for op in operations:
        if op[0] == 'I':
            hq.heappush(li1, int(op[2:]))
            hq.heappush(li2, -int(op[2:]))
            cnt_i += 1
        else:
            if op[2:] == '-1':
                try:
                    hq.heappop(li1)
                    cnt_d += 1
                except:
                    pass
            else:
                try:
                    hq.heappop(li2)
                    cnt_d += 1
                except:
                    pass

    if cnt_i > cnt_d:
        return([-hq.heappop(li2), hq.heappop(li1)])
    else:
        return([0, 0])

#print(solution1(operations))
#print(solution1(operations1))
#print(solution1(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]))



### 통과
def solution(operations):
    import heapq as hq
    li = []
    cnt_i = 0; cnt_d = 0

    for op in operations:
        tmp = []
        if op[0] == 'I':
            hq.heappush(li, int(op[2:]))
            cnt_i += 1
        else:
            if op[2:] == '1':
                try:
                    for idx in range(len(li) - 1):
                        hq.heappush(tmp, hq.heappop(li))
                    li = tmp
                    cnt_d += 1
                except:
                    pass
            else:
                try:
                    hq.heappop(li)
                    cnt_d += 1
                except:
                    pass
        #print(li, cnt_i, cnt_d)

    if cnt_i > cnt_d:
        return([max(li), hq.heappop(li)])
    else:
        return([0, 0])
    

print(solution(operations))
print(solution(operations1))
print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]))