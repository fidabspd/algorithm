N1 = 5;  stages1 = [2, 1, 2, 6, 2, 4, 3, 3]  # [3,4,2,1,5]
N2 = 4;  stages2 = [4,4,4,4,4]  # [4,1,2,3]


### 시간초과
def solution_0(N, stages):
    per = dict()
    clear = []
    fail = []
    for i in range(1, N+1):
        clear = sum(list(map(lambda s: s >= i, stages)))
        fail = sum(list(map(lambda s: s == i, stages)))
        if clear == 0:
            per[f'{i}'] = 0
        else:
            per[f'{i}'] = fail/clear
    per_str = sorted(per, key=lambda x: per[x], reverse=True)
    return list(map(lambda x: int(x), per_str))


def solution(N, stages):
    clear = [0]*N
    for s in stages:
        for i in range(0, s-1):
            clear[i] += 1

    per = []
    before = len(stages)
    for c in clear:
        if before == 0:
            per.append(0)
        else:
            per.append((before-c)/before)
        before = c
        
    return sorted(list(range(1, N+1)), key=lambda x: per[x-1], reverse=True)


print(solution(N1, stages1))
print(solution(N2, stages2))


def solution_else(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)
