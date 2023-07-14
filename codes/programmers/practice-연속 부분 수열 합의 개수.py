# https://school.programmers.co.kr/learn/courses/30/lessons/131701
elements = [7, 9, 1, 1, 4]  # 18


def solution(elements):
    unique_sum = set()
    tmp_elements = [0] * len(elements)
    for length in range(1, len(elements) // 2 + 1):
        for i in range(len(elements)):
            new_add = elements[(i + length - 1) % len(elements)]
            tmp_elements[i] += new_add
            unique_sum.add(tmp_elements[i])
    total = sum(elements)
    unique_sum = list(unique_sum)
    unique_sum += [total - _sum for _sum in unique_sum + [0]]

    return len(set(unique_sum))


print(solution(elements))
