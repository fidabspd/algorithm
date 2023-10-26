N0 = 11
stations0 = [4, 11]
W0 = 1  # 3
N1 = 16
stations1 = [9]
W1 = 2  # 3


def solution(N, stations, W):
    stations.sort()
    c = W * 2 + 1
    old_e = -1
    answer = 0
    for station in stations:
        station -= 1
        s, e = max(0, station - W), min(station + W, N - 1)
        if s > old_e:
            not_covered = s - old_e - 1
            d, m = divmod(not_covered, c)
            answer += d + int(bool(m))
        old_e = e
    not_covered = N - 1 - old_e
    d, m = divmod(not_covered, c)
    answer += d + int(bool(m))

    return answer


print(solution(N0, stations0, W0))
print(solution(N1, stations1, W1))
