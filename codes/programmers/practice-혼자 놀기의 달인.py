# https://school.programmers.co.kr/learn/courses/30/lessons/131130
cards = [8, 6, 3, 7, 2, 5, 1, 4]  # 12


def solution(cards):
    import heapq

    now = 1
    scores = []
    score = 0
    sum_cards = sum(cards)
    while sum_cards:
        if cards[now - 1] != 0:
            sum_cards -= now
            before, now = now, cards[now - 1]
            cards[before - 1] = 0
            score += 1
        else:
            heapq.heappush(scores, -score)
            for now in range(len(cards)):
                if cards[now] != 0:
                    now += 1
                    break
            score = 0
    heapq.heappush(scores, -score)
    if len(scores) == 1:
        return 0

    answer = 1
    answer *= heapq.heappop(scores)
    answer *= heapq.heappop(scores)

    return answer


print(solution(cards))
