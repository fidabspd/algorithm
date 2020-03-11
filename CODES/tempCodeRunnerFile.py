stock = 4
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