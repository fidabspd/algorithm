people1 = [70, 50, 80, 50]; limit1 = 100  # 3
people2 = [70, 80, 50]; limit2 = 100  # 3
people3 = [1,2,3,4,5,6,7,8,9,10]; limit3 = 20  # 3

import heapq
def solution(people, limit):
    answer = 0
    num = len(people)
    _people = [-person for person in people]
    heapq.heapify(people)
    heapq.heapify(_people)
    now = 0  # 몇명 타고 나갔는지
    
    while now < num:
        #print(people[0], -_people[0], now, people[0] - _people[0] <= limit)
        if people[0] - _people[0] <= limit:
            heapq.heappop(people); heapq.heappop(_people)
            now += 2
        else:
            heapq.heappop(_people)
            now += 1
        answer += 1
        
    return answer


print(solution(people1, limit1))
print(solution(people2, limit2))
print(solution(people3, limit3))



### 다른 사람의 풀이
def solution_else(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer