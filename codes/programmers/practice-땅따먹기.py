land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]  # 16


def solution(land):
    for r in range(len(land)-1):
        for i in range(4):
            land[r+1][i] += max(land[r][:i]+land[r][i+1:])
    return max(land[-1])


print(solution(land))