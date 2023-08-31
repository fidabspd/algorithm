k0 = 5
ranges0 = [[0, 0], [0, -1], [2, -3], [3, -3]]  # [33.0,31.5,0.0,-1.0]
k1 = 3
ranges1 = [[0, 0], [1, -2], [3, -3]]  # [47.0,36.0,12.0]


def solution(k, ranges):
    def get_sum_tmp(k):
        sum_tmp = []
        while k != 1:
            before = k
            if k % 2 == 0:
                k //= 2
            else:
                k = 3 * k + 1
            sum_tmp.append((before + k) / 2)
        return sum_tmp

    def get_answer_for_one_range(start, end):
        end += max_len
        if start > end:
            return -1
        return sum(sum_tmp[start:end])

    sum_tmp = get_sum_tmp(k)
    max_len = len(sum_tmp)
    answer = []
    for start, end in ranges:
        answer.append(float(get_answer_for_one_range(start, end)))

    return answer


print(solution(k0, ranges0))
print(solution(k1, ranges1))
