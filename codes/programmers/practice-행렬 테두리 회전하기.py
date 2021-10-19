rows1 = 6; columns1 = 6; queries1 = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]  # [8, 10, 25]
rows2 = 3; columns2 = 3; queries2 = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]  # [1, 1, 5, 3]
rows3 = 100; columns3 = 97; queries3 = [[1,1,100,97]]  # [1]


def solution(rows, columns, queries):
    import numpy as np
    arr = np.array(range(1, rows*columns+1)).reshape(rows, columns)

    answer = []
    for r1, c1, r2, c2 in queries:
        r1, r2, c1, c2 = r1-1, r2-1, c1-1, c2-1
        rot1, rot2, rot3, rot4 = arr[r1, c1:c2].tolist(), arr[r1:r2, c2].tolist(), arr[r2, c1+1:c2+1].tolist(), arr[r1+1:r2+1, c1].tolist()
        arr[r1, c1+1:c2+1], arr[r1+1:r2+1, c2], arr[r2, c1:c2], arr[r1:r2, c1] = rot1, rot2, rot3, rot4
        answer.append(min(rot1+rot2+rot3+rot4))
    
    return answer


print(solution(rows1, columns1, queries1))
print(solution(rows2, columns2, queries2))
print(solution(rows3, columns3, queries3))