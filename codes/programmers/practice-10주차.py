line1 = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
# ["....*....", ".........", ".........", "*.......*", ".........", ".........", ".........", ".........", "*.......*"]
line2 = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]  # ["*.*"]
line3 = [[1, -1, 0], [2, -1, 0]]  # ["*"]
line4 = [[1, -1, 0], [2, -1, 0], [4, -1, 0]]  # ["*"]


def solve_eq(eq1, eq2):
    a, b, e = eq1
    c, d, f = eq2

    if (a*d-b*c) == 0:
        x, y = 0.1, 0.1
    else:
        x = (b*f-e*d)/(a*d-b*c)
        y = (e*c-a*f)/(a*d-b*c)
    return x, y


def solution(line):
    loc = []
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            x, y = solve_eq(line[i], line[j])
            if (int(x), int(y)) == (x, y) and (int(x), int(y)) not in loc:
                loc.append((int(x), int(y)))

    tmp = [i for i in zip(*loc)]
    min_x, max_x, min_y, max_y = min(tmp[0]), max(tmp[0]), min(tmp[1]), max(tmp[1])
    loc = [(-(j-max_y), i-min_x) for i, j in loc]

    row = ['.'] * (max_x-min_x+1)
    answer = []
    for _ in range(max_y-min_y+1):
        answer.append(row.copy())
    for x, y in loc:
        answer[x][y] = '*'
    answer = list(map(lambda x: ''.join(x), answer))
    
    return answer


print(solution(line1))
print(solution(line2))
print(solution(line3))
print(solution(line4))