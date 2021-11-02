orders1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]; course1 = [2,3,4]  # ["AC", "ACDE", "BCFG", "CDE"]
orders2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]; course2 = [2,3,5]  # ["ACD", "AD", "ADE", "CD", "XYZ"]
orders3 = ["XYZ", "XWY", "WXA"]; course3 = [2,3,4]  # ["WX", "XY"]


def solution(orders, course):
    from itertools import combinations
    answer = []
    for i in course:
        dct = {}
        for o in orders:
            for can in combinations(o, i):
                can = ''.join(sorted(list(can)))
                if can in dct.keys():
                    dct[can] += 1
                else:
                    dct[can] = 1
        tmp = []
        for k in dct.keys():
            if (dct[k]==max(dct.values()) and max(dct.values())>1):
                tmp.append(k)
        answer.extend(tmp)
    return sorted(answer)


print(solution(orders1, course1))
print(solution(orders2, course2))
print(solution(orders3, course3))