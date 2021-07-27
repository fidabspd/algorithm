n1 = 4  # [1,2,9,3,10,8,4,5,6,7]
n2 = 5  # [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
n3 = 6  # [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]


def solution(n):
    tri = []
    for i in range(1, n+1):
        tri.append([0]*i)

    direction = -1
    i, j = -1, 0
    now = 0

    for count in range(n, 0, -1):
        direction += 1
        for _ in range(count):
            now += 1
            if direction%3 == 0:
                i += 1
            elif direction%3 == 1:
                j += 1
            else:
                i -= 1; j -= 1
            tri[i][j] = now

    answer = []
    for l in tri:
        answer.extend(l)

    return answer


print(solution(n1))
print(solution(n2))
print(solution(n3))
