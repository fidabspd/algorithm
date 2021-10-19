tickets1 = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]  # [ICN, JFK, HND, IAD]
tickets2 = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]  # [ICN, ATL, ICN, SFO, ATL, SFO]


def solution(tickets):
    answers = [[i] for i, ticket in enumerate(tickets) if ticket[0] == 'ICN']
    
    while max(list(map(len, answers))) < len(tickets):
        new_answers = []
        for answer in answers:
            for i, ticket in enumerate(tickets):
                if i not in answer and ticket[0] == tickets[answer[-1]][-1]:
                    new_answer = answer.copy()
                    new_answer.append(i)
                    new_answers.append(new_answer)
        answers = new_answers
    
    answers_str = []
    for answer in answers:
        answer_str = ['ICN']
        for i in answer:
            answer_str += [tickets[i][1]]
        answers_str.append(answer_str)

    return min(answers_str)


### DFS 풀이
from collections import defaultdict
def dfs(graph, N, key, footprint):
    if len(footprint) == N + 1:
        return footprint
    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx)
        tmp = footprint.copy()
        tmp.append(country)
        ret = dfs(graph, N, country, tmp)
        graph[key].insert(idx, country)
        if ret:
            return ret

def solution_else(tickets):
    answer = []
    graph = defaultdict(list)
    N = len(tickets)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort()
    answer = dfs(graph, N, "ICN", ["ICN"])
    return answer


print(solution(tickets1))
print(solution(tickets2))