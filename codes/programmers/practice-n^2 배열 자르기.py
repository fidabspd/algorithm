n1 = 3; left1 = 2; right1 = 5  # [3,2,2,3]
n2 = 4; left2 = 7; right2 = 14  # [4,3,3,3,4,4,4,4]


### 시간 초과
def solution_0(n, left, right):
    answer_tmp = [[i if i > j else j for i in range(1, n+1)] for j in range(1, n+1)]
    answer = []
    for a in answer_tmp:
        answer.extend(a)
    return answer[left:right+1]


### 통과
def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        answer.append(max(divmod(i, n)) + 1)
    return answer


print(solution(n1, left1, right1))
print(solution(n2, left2, right2))