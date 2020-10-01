clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]


import numpy as np
import collections as co

def solution1(clothes):
    tmp = 1
    for i in co.Counter(np.array(clothes)[:, -1]).values():
        tmp *= i + 1
    return tmp - 1

print(solution1(clothes))


# 프로그래머스 다른 풀이
def solution2(clothes):
    from functools import reduce
    from collections import Counter
    cnt = Counter([kind for name, kind in clothes]).values()  # name, kind로 2차원 배열을 풀고 kind만 남김
    answer = reduce(lambda x, y: x * (y + 1), cnt, 1) - 1  # reduce의 초기값을 1로 주고 y에만 1을 더하며 곱함
    return answer

print(solution2(clothes))