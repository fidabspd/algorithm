sequence0 = [1, 2, 3, 4, 5]
k0 = 7  # [2, 3]
sequence1 = [1, 1, 1, 2, 3, 4, 5]
k1 = 5  # [6, 6]
sequence2 = [2, 2, 2, 2, 2]
k2 = 6  # [0, 2]


def solution(sequence, k):
    answer = []
    _sum = sequence[0]
    s = 0
    e = 1
    while s < len(sequence):
        if e == len(sequence) and _sum < k:
            break

        if _sum < k:
            e += 1
            _sum += sequence[e - 1]
        elif _sum > k:
            _sum -= sequence[s]
            s += 1
        elif _sum == k:
            answer.append([s, e - 1])
            _sum -= sequence[s]
            s += 1
    return sorted(answer, key=lambda x: (x[1] - x[0], x[0]))[0]


print(solution(sequence0, k0))
print(solution(sequence1, k1))
print(solution(sequence2, k2))
