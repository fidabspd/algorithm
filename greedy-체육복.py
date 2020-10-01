# def solution(n, lost, reserve):
#     answer = 0
#     return answer

n1 = 5; lost1 = [2, 4]; reserve1 = [1, 3, 5]  # return 5
n2 = 5; lost2 = [2, 4]; reserve2 = [3]  # return 4
n3 = 3; lost3 = [3]; reserve3 = [1]  # return 2


n = 5; lost = [1, 2, 3]; reserve = [1, 2, 3]

def solution(n, lost, reserve):
    answer = 0
    lost_c = lost.copy()
    
    for l in lost_c:
        if l in reserve:  # 여분있는애가 도둑맞으면
            lost.remove(l); reserve.remove(l)
    answer += n - len(lost)
    for l in lost:
        
        if len(reserve) == 0:
            break
            
        if l-1 in reserve:  # 왼쪽애가 여분 있으면
            answer += 1
            reserve.remove(l-1)
        elif l+1 in reserve:  # 오른쪽애가 여분 있으면
            answer += 1
            reserve.remove(l+1)
            
    return answer

print(solution(n, lost, reserve))