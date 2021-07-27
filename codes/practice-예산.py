d1 = [1,3,2,5,4]; budget1 = 9  # 3
d2 = [2,2,3,3]; budget2 = 10  # 4


def solution(d, budget):
    if sum(d) <= budget:
        return len(d)
    total = 0
    for i, d_ in enumerate(sorted(d)):
        total += d_
        if total > budget:
            break
    return i


print(solution(d1, budget1))
print(solution(d2, budget2))
