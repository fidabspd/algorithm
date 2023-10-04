arr0 = [
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 1, 1, 1],
]  # [4, 9]
arr1 = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
]  # [10, 15]


def solution(arr):
    def check_arr(sr, er, sc, ec):
        _sum = 0
        for a in arr[sr:er]:
            _sum += sum(a[sc:ec])
        dim = er - sr
        if _sum == dim * dim:
            return 1
        elif _sum == 0:
            return 0
        else:
            return None

    answer = [0, 0]
    arr_len = len(arr)
    stack = [[0, arr_len, 0, arr_len]]
    while stack:
        sr, er, sc, ec = stack.pop()
        checked = check_arr(sr, er, sc, ec)
        if checked is None:
            stack.append([sr, (sr + er) // 2, sc, (sc + ec) // 2])
            stack.append([(sr + er) // 2, er, sc, (sc + ec) // 2])
            stack.append([sr, (sr + er) // 2, (sc + ec) // 2, ec])
            stack.append([(sr + er) // 2, er, (sc + ec) // 2, ec])
        elif checked == 0:
            answer[0] += 1
        elif checked == 1:
            answer[1] += 1
    return answer


print(solution(arr0))
print(solution(arr1))
