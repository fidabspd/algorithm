import sys

n, r, c = map(int, sys.stdin.readline().split(' '))


def solution(n, r, c):
    answer = 0
    quadrant = {(0, 0): 0, (0, 1): 1, (1, 0): 2, (1, 1): 3}
    while n > 0:
        x, r = divmod(r, 2**(n-1))
        y, c = divmod(c, 2**(n-1))
        answer += quadrant[(x, y)]*((2**(n-1))**2)
        n -= 1

    return answer


print(solution(n, r, c))
