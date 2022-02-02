n1 = 5; info1 = [2,1,1,1,0,0,0,0,0,0,0]  # [0,2,2,0,1,0,0,0,0,0,0]
n2 = 1; info2 = [1,0,0,0,0,0,0,0,0,0,0]  # [-1]
n3 = 9; info3 = [0,0,1,2,0,1,1,1,1,1,1]  # [1,1,2,0,1,2,2,0,0,0,0]
n4 = 10; info4 = [0,0,0,0,0,0,0,0,3,4,3]  # [1,1,1,1,1,1,1,1,0,0,2]

def comp(info, score):
    ap_s = 0; li_s = 0
    i = 10
    for ap, li in zip(info, score):
        if ap+li == 0:
            continue
        if li > ap:
            li_s += i
        else:
            ap_s += i
        i -= 1
    return li_s - ap_s

def solution(n, info):
    answer = []
    return answer


print(solution(n1, info1))
print(solution(n2, info2))
print(solution(n3, info3))
print(solution(n4, info4))