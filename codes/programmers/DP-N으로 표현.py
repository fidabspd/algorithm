N1 = 5; number1 = 12  # 4
N2 = 2; number2 = 11  # 3

        
def cal(list1, list2, cal_result):
    cal_result_updated = cal_result.copy()
    for i in range(len(list1)):
        for j in range(len(list2)):
            cal_result_updated.extend([
                list1[i] + list2[j],
                list1[i] * list2[j],
                list1[i] - list2[j],
                list2[j] - list1[i],
            ])
            if list1[i] != 0:
                cal_result_updated.extend([
                    list2[j] // list1[i],
                ])
            if list2[j] != 0:
                cal_result_updated.extend([
                    list1[i] // list2[j],
                ])
    return cal_result_updated


def solution(N, number):
    if N == number:
        return 1
    cal_result_dict = {
        1: [N]
    }
    for length in range(2, 9):
        cal_result_dict[length] = [
            N * eval('1'*length)
        ]
        for j, k in [(i, length-i) for i in range(1, length)]:
            cal_result_dict[length] = \
                cal(cal_result_dict[j], cal_result_dict[k], cal_result_dict[length])
        cal_result_dict[length] = list(set(cal_result_dict[length]))
        if number in cal_result_dict[length]:
            return length
    return -1
    
    
print(solution(N1, number1))
print(solution(N2, number2))