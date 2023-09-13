players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]  # ["mumu", "kai", "mine", "soe", "poe"]


def solution(players, callings):
    name_rank = {name: rank for rank, name in enumerate(players)}
    rank_name = {rank: name for rank, name in enumerate(players)}
    for calling in callings:
        now_rank = name_rank[calling]
        lose = rank_name[now_rank - 1]
        name_rank[calling] -= 1
        name_rank[lose] += 1
        rank_name[now_rank] = lose
        rank_name[now_rank - 1] = calling
    return list(rank_name.values())


print(solution(players, callings))
