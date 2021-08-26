relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],\
    ["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
#2


def combi(arr, n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        rest_arr = arr[i+1:]
        for C in combi(rest_arr, n-1):
            result.append([arr[i]]+C)
    return result

def solution(relation):
    unique_key = []
    for n_key in list(range(1, len(relation[0])+1)):
        combis = combi(list(range(len(relation[0]))), n_key)
        for combi_result in combis:
            continue_ = False
            for key in unique_key:
                if len(set(combi_result+key)) == len(combi_result):
                    continue_ = True
                    break
            if continue_:
                continue
            candi = [[keys[c] for c in combi_result] for keys in relation]
            is_unique = True
            for i in range(len(candi)):
                if candi[i] in candi[:i]+candi[i+1:]:
                    is_unique = False
                    break
            if is_unique:
                unique_key.append(combi_result)
    return len(unique_key)


print(solution(relation))
print(solution([['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']]))


def solution_else(relation):
    answer_list = list()
    for i in range(1, 1 << len(relation[0])):
        tmp_set = set()
        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                if i & (1 << k):
                    tmp += str(relation[j][k])
            tmp_set.add(tmp)

        if len(tmp_set) == len(relation):
            not_duplicate = True
            for num in answer_list:
                if (num & i) == num:
                    not_duplicate = False
                    break
            if not_duplicate:
                answer_list.append(i)
    return len(answer_list)
