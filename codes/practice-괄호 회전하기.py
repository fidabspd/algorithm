s1 = "[](){}"  # 3
s2 = "}]()[{"  # 2
s3 = "[)(]"  # 0
s4 = "}}}"  # 0


def is_right(s):
    after = ''
    for i in s:
        after += i
        if after[-2:] in ['[]', '()', '{}']:
            after = after[:-2]
    return not bool(after)

def solution(s):
    answer = 0
    for i in range(len(s)):
        s = s[1:]+s[:1]
        if is_right(s):
            answer += 1
    return answer


print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))