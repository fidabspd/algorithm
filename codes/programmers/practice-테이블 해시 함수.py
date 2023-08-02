# https://school.programmers.co.kr/learn/courses/30/lessons/147354
data = [
    [2, 2, 6],
    [1, 5, 10],
    [4, 2, 9],
    [3, 8, 3],
]
col = 2
row_begin = 2
row_end = 3  # 4


def solution(data, col, row_begin, row_end):
    answer = 0

    data = sorted(data, key=lambda x: (x[col - 1], -x[0]))
    for i in range(row_begin - 1, row_end):
        tmp = 0
        for d in data[i]:
            tmp += d % (i + 1)
        answer ^= tmp
    return answer


print(solution(data, col, row_begin, row_end))
