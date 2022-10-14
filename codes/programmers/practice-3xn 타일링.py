def solution(n):
    if n % 2 == 1 or n == 0:
        return 0

    dp = [3, 11]
    while len(dp) < n // 2 + 1:
        dp.append(((dp[-1] * 4) % 1000000007 - dp[-2]) % 1000000007)
    return dp[n // 2 - 1]


print(solution(2))  # 3
print(solution(4))  # 11
print(solution(6))  # 41


def solution_else(n):
    if n % 2 == 1 or n == 0:
        return 0

    b, f = 1, 1
    for _ in range(n // 2):
        b, f = f, (f * 4 - b) % 1000000007
    return f
