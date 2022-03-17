m = 4; n = 3; puddles = [[2, 2]]  # 4


def solution(m, n, puddles):
    arr = [[0]*m for _ in range(n)]
    arr[0][0] = 1
    puddles += [[1, 1]]
    for j in range(n):
        for i in range(m):
            if [i+1, j+1] in puddles:
                continue
            if j < 1:
                up = 0
            else:
                up = arr[j-1][i]
            if i < 1:
                left = 0
            else:
                left = arr[j][i-1]
            arr[j][i] = up + left
            
    return arr[-1][-1] % 1000000007


print(solution(m, n, puddles))
