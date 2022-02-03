id_list1 = ["muzi", "frodo", "apeach", "neo"]
report1 = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k1 = 2  # [2,1,1,0]
id_list2 = ["con", "ryan"]
report2 = ["ryan con", "ryan con", "ryan con", "ryan con"]
k2 = 3  # [0,0]


def solution(id_list, report, k):
    answer = [0]*len(id_list)
    result = {i: [] for i in id_list}
    for r in set(report):
        res, i = r.split(' ')
        result[i].append(res)
    for i in result.keys():
        if len(result[i])>=k:
            for res in result[i]:
                answer[id_list.index(res)] += 1
    return answer


print(solution(id_list1, report1, k1))
print(solution(id_list2, report2, k2))
