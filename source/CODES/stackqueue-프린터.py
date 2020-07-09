priorities = [2, 1, 3, 2]
location = 2
# return1 = 1

priorities2 = [1, 1, 9, 1, 1, 1]
location2 = 0
# return2 = 5


### 통과
def solution(priorities, location):
    idx = list(range(len(priorities)))
    for i in range(len(priorities)):
        # print(i + 1)
        
        tmp = priorities.index(max(priorities))  # max값의 index

        idx = idx[tmp:] + idx[:tmp]
        priorities = priorities[tmp:] + priorities[:tmp]
        # print(idx)
        # print(priorities)
        if idx[0] == location:
            # print(i + 1)
            break
        idx.pop(0)
        priorities.pop(0)
    return i + 1

print(solution(priorities, location))
print(solution(priorities2, location2))



### 프로그래머스 다른 풀이
def solution(p, l):
    ans = 0
    m = max(p)
    while True:
        v = p.pop(0)
        if m == v:  # max와 첫번째 값이 같고
            ans += 1
            if l == 0:  # location이 0이면 루프 멈춤
                break
            else:
                l -= 1  # 아니면 location에 1 빼기
            m = max(p)
        else:
            p.append(v)  # 첫번째 값이 max가 아니면 뒤로 보냄
            if l == 0:
                l = len(p)-1  # location값을 계속해서 업데이트
            else:
                l -= 1
    return ans
