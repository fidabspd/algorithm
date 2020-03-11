stock = 4
dates = [4,10,15]
supplies = [20,5,10]
k = 30
# result 2


### 알고리즘 잘못 이해
def solution1(stock, dates, supplies, k):
    answer = 0
    for i in range(len(dates)):
        if i == len(dates) - 1:
            if stock - dates[i] < k - dates[i]:
                stock += supplies[i]
                answer += 1
                # print(i + 1)
        else:
            if stock - dates[i] < dates[i + 1] - dates[i]:
                stock += supplies[i]
                answer += 1
                # print(i + 1)
        if i == 0:
            stock -= dates[i]
        else:
            stock -= (dates[i] - dates[i - 1])
        # print(stock, '\n')
    
    return answer

# print(solution1(stock, dates, supplies, k))



### 틀림
def solution2(stock, dates, supplies, k):
    import heapq
    stock = -stock
    k = -k
    answer = 0
    supplies = list(map(lambda x: x * -1, supplies))
    heapq.heapify(supplies)
    # print('\n\n', stock)
    for i in range(len(supplies)):
        answer += 1
        m = heapq.heappop(supplies)
        stock += m
        # print(stock)
        if stock < k:
            break
    return answer

# print(solution2(stock, dates, supplies, k))



### 분기점은 맞음
answer = 0
# print('\n\n', stock)
if stock < dates[1]:
    stock += supplies[0]
    answer += 1
else:
    if stock + supplies[1] < dates[2]:
        stock += supplies[0]
        answer += 1
    else:
        if supplies + supplies[1] + supplies[2] < k:
            stock += supplies[0]
            answer += 1
        else:
            pass
# print(stock)
if stock < dates[2]:
    stock += supplies[1]
    answer += 1
else:
    if stock + supplies[2] < k:
        stock += supplies[1]
        answer += 1
    else:
        pass
# print(stock)
if stock < k:
    stock += supplies[2]
    answer += 1
# print(stock)
# print(answer)


## 공급을 받으면 해당 공급날, 공급량을 리스트에서 없애고 stock에 더한다
##     예를 들어 첫 stock이 4였고 4일날 20을 공급받으면
##         stock = 24, dates = [10, 15], supplies = [5, 10]으로 만든다.
## 공급을 받는 기준은 가장가까운 공급날의 다음 공급날 (dates[1])보다 stock이 적으면
##     무조건 가장가까운 공급날 공급을 받아야한다.
## 그렇지 않고 만약 stock > dates[1]이라면
##     stock = 24, dates = [15], supplies = [10]으로 만들고 supplies[0]이었던 5는 킵한다
## 만약 stock > k라면 끝 아니라면 남은 공급량 10과 5중 큰 공급량을 우선적으로 stock에 더해가며 k < stock이 되는순간 멈춘다




import heapq
answer = 0
can = []
heapq.heapify(can)
for i in range(len(dates)):
    if len(dates) > 0 and stock <= dates[0]:
        dates.pop(0)
        can.append(supplies.pop(0))
        print('!', can)
        stock += can.pop(0)
        print('!', can)
        answer += 1
    else:
        dates.pop(0)
        can.append(supplies.pop(0))
    print(dates, supplies, stock)
    if stock > k:
        break


print(answer)



# stock = 4
# dates = [4,10,15]
# supplies = [20,5,10]
# k = 30


# def solution(stock, dates, supplies, k):
#     import heapq

#     answer = 0
#     heap = []

#     while stock < k:
#         while len(dates) > 0 and dates[0] <= stock:  # dates 길이만큼 돌되, stock이 다음 공급일까지 버틸수 있을때
#             dates.pop(0)
#             heapq.heappush(heap, -supplies.pop(0))  # 바로다음다음 공급일까지 못버티면 바로다음 공급일에 무조건 공급을 받게 되어있음
#             # print(heap)

#         stock -= heapq.heappop(heap)
#         answer += 1

#     return answer


# print(solution(stock, dates, supplies, k))