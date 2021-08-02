triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]  # 30


def solution(triangle):
    if len(triangle) == 1:
        return triangle[0][0]

    for i in range(len(triangle)-1):
        triangle[-2][i] += max(triangle[-1][i:i+2])
    triangle = triangle[:-1]
    return solution(triangle)


print(solution(triangle))
