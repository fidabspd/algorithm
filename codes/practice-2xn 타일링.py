### 시간 초과
def factorial_stop(start, count):
    if count == 0:
        return 1
    result = 1
    while count > 0:
        result *= start
        start -= 1
        count -= 1
        
    return result
def solution(n):
    answer = 0
    i = 0
    for i in range((n//2)+1):
        answer += factorial_stop(n-i, i)//factorial_stop(i, i)
    return answer%1000000007

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))


### 다른사람 풀이 참고
def solution_else(n):
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, (a+b)%1000000007
    return b
