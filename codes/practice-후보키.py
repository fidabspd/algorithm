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
    answer = 0
    unique_key = []
    for n_key in list(range(1, len(relation[0])+1)):
        combis = combi(list(range(len(relation[0]))), n_key)
        is_unique_list = []
        for combi_result in combis:
            candi = [[keys[c] for c in combi_result] for keys in relation]
            is_unique = True
            for i in range(len(candi)):
                if candi[i] in candi[:i]+candi[i+1:]:
                    is_unique = False
                    break
            is_unique_list.append(is_unique)
        unique_key.append([combis[i] for i in range(len(combis)) if is_unique_list[i]])

    for key in unique_key:
        print(key)


print(solution(relation))
# print(solution([['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']]))
