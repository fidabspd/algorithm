n1 = 4  # 5
n2 = 3  # 3


def solution(n):
    dp = [1, 2]
    for i in range(2, n):
        dp.append((dp[i - 2] + dp[i - 1]) % 1234567)
    return dp[n - 1]


print(solution(n1))
print(solution(n2))


def solution_else(n):
    if n == 1:
        return 1
    a, b = 1, 2
    for _ in range(2, n):
        a, b = b, (a + b) % 1234567
    return b
