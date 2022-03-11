n1 = 5; info1 = [2,1,1,1,0,0,0,0,0,0,0]  # [0,2,2,0,1,0,0,0,0,0,0]
n2 = 1; info2 = [1,0,0,0,0,0,0,0,0,0,0]  # [-1]
n3 = 9; info3 = [0,0,1,2,0,1,1,1,1,1,1]  # [1,1,2,0,1,2,2,0,0,0,0]
n4 = 10; info4 = [0,0,0,0,0,0,0,0,3,4,3]  # [1,1,1,1,1,1,1,1,0,0,2]

from itertools import combinations

def score_gap(ap, li):
    ap_t, li_t = 0, 0
    for i, (a, l) in enumerate(zip(ap, li)):
        if (a, l) == (0, 0):
            continue
        if a < l:
            li_t += 10-i
        else:
            ap_t += 10-i
    return li_t-ap_t

def low_score_shot_count(scores):
    for i, s in enumerate(scores[::-1]):
        if s != 0:
            return i, s

def solution(n, info):
    answer = []
    gap = 0
    for i in range(1, n+1):
        for comb in combinations(list(range(1, 11)), i):
            li_scores = [0 if 10-i not in comb else info[i]+1 for i in range(11)]
            if sum(li_scores) > n:
                continue
            else:
                li_scores[-1] = n-sum(li_scores)
            gap_tmp = score_gap(info, li_scores)
            if gap <= gap_tmp and gap_tmp != 0:
                if gap < gap_tmp:
                    gap = gap_tmp
                    answer = []
                answer.append(li_scores)
    
    if len(answer) == 0:
        return [-1]
    else:
        answer = sorted(answer, key=low_score_shot_count)
        return answer[0]


print(solution(n1, info1))
print(solution(n2, info2))
print(solution(n3, info3))
print(solution(n4, info4))