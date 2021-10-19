def solution(a, b):
    tmp = [a, b]
    tmp.sort()
    answer = 0
    for val in range(tmp[0], tmp[1]+1):
        answer += val
    return answer

# 다른 사람의 풀이
def adder(a, b):
    # 함수를 완성하세요
    if a > b: a, b = b, a

    return sum(range(a,b+1))