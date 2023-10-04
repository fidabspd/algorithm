n0 = 8
m0 = 4
section0 = [2, 3, 6]  # 2
n1 = 5
m1 = 4
section1 = [1, 3]  # 1
n2 = 4
m2 = 1
section2 = [1, 2, 3, 4]  # 4


def solution(n, m, section):
    answer = 0
    while section:
        fr = section[-1]
        to = fr - m
        while section and section[-1] > to:
            section.pop()
        answer += 1
    return answer


print(solution(n0, m0, section0))
print(solution(n1, m1, section1))
print(solution(n2, m2, section2))
