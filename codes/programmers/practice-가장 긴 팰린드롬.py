# https://school.programmers.co.kr/learn/courses/30/lessons/12904
s0 = "abcdcba"  # 7
s1 = "abacde"  # 3


def solution_timeover(s):
    def check(sub_s):
        len_sub_s = len(sub_s)
        for i in range(len_sub_s // 2):
            if sub_s[i] != sub_s[-i - 1]:
                return False
        return True

    len_s = len(s)
    s_reverse = list(s)
    s_reverse.reverse()
    dp = [[0] * (len_s + 1) for _ in range(len_s + 1)]
    candi = []
    for i in range(len_s):
        for j in range(len_s):
            if s[i] == s_reverse[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
                candi.append(s[i - dp[i + 1][j + 1] + 1 : i + 1])

    answer = 0
    candi.sort(key=len, reverse=True)
    for c in candi:
        if check(c):
            answer = len(c)
            break
    return answer


def solution(s):
    def check_odd(base_idx):
        i = 0
        while 0 <= base_idx - (i + 1) and base_idx + (i + 1) < len(s):
            if s[base_idx - (i + 1)] == s[base_idx + (i + 1)]:
                i += 1
            else:
                break
        return i * 2 + 1

    def check_even(base_idx):
        if base_idx == len(s) - 1:
            return 1
        i = 0
        while 0 <= base_idx - i and base_idx + (i + 1) < len(s):
            if s[base_idx - i] == s[base_idx + (i + 1)]:
                i += 1
            else:
                break
        return i * 2

    answer = 0
    for base_idx in range(len(s)):
        answer = max(answer, check_odd(base_idx), check_even(base_idx))

    return answer


print(solution(s0))
print(solution(s1))
