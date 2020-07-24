tickets1 = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]  # [ICN, JFK, HND, IAD]
tickets2 = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]  # [ICN, ATL, ICN, SFO, ATL, SFO]


# 틀림
def solution(tickets):
    
    tickets.sort()
    now = 'ICN'
    tmp = []

    while tickets:
        for ticket in tickets:
            while now not in [ticket[0] for ticket in tickets]:
                tickets.append(tmp.pop())
            if ticket[0] == now:
                tmp.append(tickets.pop(tickets.index(ticket)))
                now = ticket[1]
                break
        print(f'tmp: {tmp}, tickets: {tickets}')

    return [t[0] for t in tmp] + [tmp[-1][1]]

print(solution(tickets1))
print(solution(tickets2))