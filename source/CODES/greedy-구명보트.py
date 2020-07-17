people1 = [70, 50, 80, 50]; limit1 = 100  # 3
people2 = [70, 80, 50]; limit2 = 100  # 3
people3 = [1,2,3,4,5,6,7,8,9,10]; limit3 = 20  # 3

import heapq
def solution(people, limit):
    people = [-p for p in people]
    people = heapq.heapify(people)
    lst = []
    
    _limit = -limit
    while people:
        tmp = heapq.heappop(people)
        if tmp >= _limit:
            _limit += tmp
        else:
            heapq.heappush(lst, tmp)
    
    

# print(solution(people1, limit1))
# print(solution(people2, limit2))
print(solution(people3, limit3))