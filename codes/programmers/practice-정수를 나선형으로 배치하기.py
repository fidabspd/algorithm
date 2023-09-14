n0 = 4  # [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
n1 = 5  # [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]


def solution(n):
    def check_valid_point(i, j):
        if not 0 <= i < n:
            return False
        elif not 0 <= j < n:
            return False
        elif answer[i][j]:
            return False
        else:
            return True

    def get_next_point(i, j, d):
        dest_i = i + move[d][0]
        dest_j = j + move[d][1]
        if not check_valid_point(dest_i, dest_j):
            d = (d + 1) % 4
            dest_i, dest_j, d = get_next_point(i, j, d)
        return dest_i, dest_j, d

    move = {
        0: (0, 1),
        1: (1, 0),
        2: (0, -1),
        3: (-1, 0),
    }
    answer = [[0] * n for _ in range(n)]
    i, j, d = 0, -1, 0
    now = 0
    for now in range(1, n**2 + 1):
        i, j, d = get_next_point(i, j, d)
        answer[i][j] = now

    return answer


print(solution(n0))
print(solution(n1))
