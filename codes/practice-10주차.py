line1 = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
# ["....*....", ".........", ".........", "*.......*", ".........", ".........", ".........", ".........", "*.......*"]
line2 = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]  # ["*.*"]
line3 = [[1, -1, 0], [2, -1, 0]]  # ["*"]
line4 = [[1, -1, 0], [2, -1, 0], [4, -1, 0]]  # ["*"]


def solve_eq(eq1, eq2):
    a1, b1, c1 = eq1
    a2, b2, c2 = eq2
    if (a1, b2) == (0, 0):
        x = -c2/a2
        y = -c1/b1
    elif (a2, b1) == (0, 0):
        x = -c1/a1
        y = -c2/b2
    elif ((a1, a2) == (0, 0)) or ((b1, b2) == (0, 0)):
        x, y = 0.1, 0.1
    else:
        x = (-b1*c2+b2*c1)/(-a2*b1+a1*b2)
        y = (a2*c1-a1*c2)/(-a2*b1+a1*b2)
    return x, y


def solution(line):
    loc_list = []
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            loc = solve_eq(line[i], line[j])
            loc_int = (int(loc[0]), int(loc[1]))
            if loc_int == loc:
                loc_list.append(loc_int)
    return list(set(loc_list))


# print(solution(line1))
# print(solution(line2))
# print(solution(line3))
# print(solution(line4))


loc_list = [(4, -4), (-4, -4), (-4, 1), (0, 4), (4, 1)]
def draw(loc_list):
    loc_list_tmp = [i for i in zip(*loc_list)]
    min_x, max_x, min_y, max_y = \
        min(loc_list_tmp[0]), max(loc_list_tmp[0]), min(loc_list_tmp[1]), max(loc_list_tmp[1])
    loc_list = [(loc[1]-min_y, loc[0]-min_x) for loc in loc_list]
    print(loc_list)
    answer = [['.']*(max_x-min_x)]*(max_y-min_y)
    for loc in loc_list:
        answer[loc[0]][loc[1]] = '*'
    answer = [''.join(a) for a in answer]
    print(answer)


print(draw(loc_list))
