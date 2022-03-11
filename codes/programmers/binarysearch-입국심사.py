n = 6; times = [7, 10]  # 28


def solution(n, times):
    answer = 0
    times.sort()
    m, M = times[0], times[-1]*n
    print(m, M)
    while m <= M:
        mid = (m+M)//2
        total = sum([mid//time for time in times])

        if total >= n:
            answer = mid
            M = mid - 1
        elif total < n:
            m = mid + 1
        print(m, M)

    return answer


print(solution(n, times))
