# https://school.programmers.co.kr/learn/courses/30/lessons/64064

user_id0 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id0 = ["fr*d*", "abc1**"]  # 2
user_id1 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id1 = ["*rodo", "*rodo", "******"]  # 2
user_id2 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id2 = ["fr*d*", "*rodo", "******", "******"]  # 3


def solution_timeover(user_id, banned_id):
    def is_matched(id, pattern):
        if len(id) != len(pattern):
            return False
        for i, j in zip(id, pattern):
            if j == "*":
                continue
            elif i == j:
                continue
            else:
                return False
        return True

    def dfs(case):
        nonlocal visited_u, visited_b, cases

        if len(case) == len(banned_id):
            cases.append(tuple(sorted(case)))
            return

        for u_idx, u in enumerate(user_id):
            if visited_u[u_idx]:
                continue
            for b_idx, b in enumerate(banned_id):
                if visited_b[b_idx]:
                    continue
                if is_matched(u, b):
                    visited_u[u_idx], visited_b[b_idx] = 1, 1
                    dfs(case + [u])
                    visited_u[u_idx], visited_b[b_idx] = 0, 0

    visited_u = [0] * len(user_id)
    visited_b = [0] * len(banned_id)
    cases = []

    dfs([])

    return len(set(cases))


def solution(user_id, banned_id):
    def is_matched(id, pattern):
        if len(id) != len(pattern):
            return False
        for i, j in zip(id, pattern):
            if j == "*":
                continue
            elif i == j:
                continue
            else:
                return False
        return True

    banned_cans = []
    for b in banned_id:
        tmp = []
        for u in user_id:
            if is_matched(u, b):
                tmp.append(u)
        banned_cans.append(tmp)

    stack = [[_] for _ in banned_cans[0]]

    n_banned = len(banned_id)
    cases = []
    while stack:
        case = stack.pop()
        n_step = len(case)
        if n_step == n_banned:
            cases.append(tuple(sorted(case)))
            continue
        for banned_can in banned_cans[n_step]:
            if banned_can in case:
                continue
            stack.append(case + [banned_can])

    return len(set(cases))


def solution_else(user_id, banned_id):
    def check(id, pattern):
        if len(id) != len(pattern):
            return False
        for i, p in zip(id, pattern):
            if p == "*":
                continue
            elif i != p:
                return False
        return True

    def dfs(case):
        if len(case) == len(banned_id):
            cases.append(tuple(sorted(case)))
            return
        spare = board[len(case)]
        for id in spare:
            if id in case:
                continue
            dfs(case + [id])

    board = []
    for b in banned_id:
        tmp = []
        for u in user_id:
            if check(u, b):
                tmp.append(u)
        board.append(tmp)

    cases = []
    dfs([])

    return len(set(cases))


print(solution(user_id0, banned_id0))
print(solution(user_id1, banned_id1))
print(solution(user_id2, banned_id2))
