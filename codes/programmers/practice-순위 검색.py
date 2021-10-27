import bisect


info = [
    "java backend junior pizza 150",\
    "python frontend senior chicken 210",\
    "python frontend senior chicken 150",\
    "cpp backend senior pizza 260",\
    "java backend junior chicken 80",\
    "python backend senior chicken 50"
]
query = [
    "java and backend and junior and pizza 100",\
    "python and frontend and senior and chicken 200",\
    "cpp and - and senior and pizza 250",\
    "- and backend and senior and - 150",\
    "- and - and - and chicken 100",\
    "- and - and - and - 150"
]
# [1,1,1,1,2,4]


### 시간 초과
def solution_0(info, query):
    answer = []
    info = list(map(lambda x: x.split(' '), info))
    query = list(map(lambda x: [i for i in x.split(' ') if i != 'and'], query))
    for q in query:
        print('\n')
        right = list(range(len(info)))
        for i in range(len(q)):
            right_for_iter = right.copy()
            for r in right_for_iter:
                print(info[r][i], q[i])
                if q[i] == '-':
                    continue
                elif i == len(q)-1:
                    if int(info[r][i]) < int(q[i]):
                        right.remove(r)
                        print(r)
                elif info[r][i] != q[i]:
                    right.remove(r)
                    print(r)
            print('remain:', right)
        answer.append(len(right))
    return answer


### 정답
from itertools import combinations
from bisect import bisect_left
def solution(info, query):

    info_dict = {'':[]}
    for i in info:
        tmp = i.split(' ')
        k, v = tmp[:-1], int(tmp[-1])
        info_dict[''].append(v)
        for c in range(1, 5):
            for key in combinations(k, c):
                key = ''.join(key)
                if key in info_dict.keys():
                    info_dict[key].append(v)
                else:
                    info_dict[key] = [v]
    for k in info_dict.keys():
        info_dict[k].sort()

    answer = []
    for q in query:
        q = [s for s in q.split(' ') if s not in ['and', '-']]
        k, v = ''.join(q[:-1]), int(q[-1])
        if k in list(info_dict.keys()):
            answer.append(len(info_dict[k])-bisect_left(info_dict[k], v))
        else:
            answer.append(0)

    return answer


print(solution(info, query))
