def solution(n):
    if n % 2 == 0:
        answer = '수박' * int(n / 2)
    else:
        answer = '수박' * int(n / 2) + '수'
    return answer

print(solution(4))
print(solution(3))


# 다른 사람의 풀이
def water_melon(n):
    s = "수박" * n
    return s[:n]