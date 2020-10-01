s1 = "pPoooyY"  # true
s2 = "Pyy"  # false

def solution(s):
    num_p = 0; num_y = 0
    for _s in s:
        if _s in ('p', 'P'):
            num_p += 1
        if _s in ('y', 'Y'):
            num_y += 1
    if num_p == num_y:
        answer = True
    else:
        answer = False
    print(num_p, num_y)
    return answer

print(solution(s1))
print(solution(s2))


# 다른 사람의 풀이
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')