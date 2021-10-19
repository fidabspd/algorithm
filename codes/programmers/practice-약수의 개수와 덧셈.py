left1 = 13; right1 = 17  # 43
left2 = 24; right2 = 27  # 52


import math
def solution(left, right):    
    answer = 0
    for i in range(left, right+1):
        if math.sqrt(i) == int(math.sqrt(i)):
            answer -= i
        else:
            answer += i
    return answer


print(solution(left1, right1))
print(solution(left2, right2))
