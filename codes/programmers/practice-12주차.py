k = 80; dungeons = [[80,20],[50,40],[30,10]]  # 3


from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for per in permutations(dungeons, len(dungeons)):
        answer_tmp = 0
        k_c = k
        for m, p in per:
            if k_c == 0:
                break
            if m > k or p > k_c:
                continue
            k_c -= p
            answer_tmp += 1
        if answer_tmp > answer:
            answer = answer_tmp
    return answer


print(solution(k, dungeons))