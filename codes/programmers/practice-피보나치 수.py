### 시간 초과
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return (fibo(n-1) + fibo(n-2)) % 1234567

def solution(n):
    return fibo(n)


### 다른사람의 풀이
def solution_else(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
        
    return a % 1234567

print(solution_else(100))
print(solution_else(3))
print(solution_else(5))
print(solution_else(40))
