sticker0 = [14, 6, 5, 11, 3, 9, 2, 10]  # 36
sticker1 = [1, 3, 2, 5, 4]  # 8
sticker2 = [14, 1, 1, 14, 1, 1, 14, 1, 1]  # 42
sticker3 = [14, 11, 8, 14, 11, 8, 14, 11, 8]  # 47


def solution(sticker):
    def check(sticker):
        sticker = sticker[:-1]
        sticker[1] = max(sticker[:2])
        for i in range(2, len(sticker)):
            sticker[i] = max(sticker[i - 1], sticker[i - 2] + sticker[i])
        return sticker[-1]

    if len(sticker) < 4:
        return max(sticker)

    answer = 0
    for i in range(2):
        answer = max(answer, check(sticker[i:] + sticker[:i]))

    return answer


print(solution(sticker0))
print(solution(sticker1))
print(solution(sticker2))
print(solution(sticker3))
