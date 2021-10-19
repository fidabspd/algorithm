arr11 = [[1, 4], [3, 2], [4, 1]]; arr21 = [[3, 3], [3, 3]]  # [[15, 15], [15, 15], [15, 15]]
arr12 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]; arr22 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]  # [[22, 22, 11], [36, 28, 18], [29, 20, 14]]


def solution(arr1, arr2):
    nrow = len(arr1)
    ncol = len(arr2[0])
    npro = len(arr1[0])
    answer = []
    for r in range(nrow):
        row = []
        for c in range(ncol):
            ij = 0
            for p in range(npro):
                ij += arr1[r][p] * arr2[p][c]
            row.append(ij)
        answer.append(row)
    return answer


print(solution(arr11, arr21))
print(solution(arr12, arr22))


def solution_else(arr1, arr2):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*arr2)] for A_row in arr1]
    