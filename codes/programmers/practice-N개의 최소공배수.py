arr1 = [2,6,8,14]  # 168
arr2 = [1,2,3]  # 6


def solution(arr):
    answer = 1
    d = 2

    while max(arr) >= d:
        is_div = [e%d == 0 for e in arr]
        if sum(is_div) >= 2:
            answer *= d
            arr = [e//d if is_d else e for e, is_d in zip(arr, is_div)]
        else:
            d += 1

    for e in arr:
        answer *= e

    return answer


print(solution(arr1))
print(solution(arr2))
        