weights1 = [50,82,75,120]; head2head1 = ["NLWL","WNLL","LWNW","WWLN"]  # [3,4,1,2]
weights2 = [145,92,86]; head2head2 = ["NLW","WNL","LWN"]  # [2,3,1]
weights3 = [60,70,60]; head2head3 = ["NNN","NNN","NNN"]  # [2,1,3]


def solution(weights, head2head):
    win_rates = []
    over_win_counts = []
    for i, head in enumerate(head2head):
        match_count = 0
        win_count = 0
        over_win_count = 0
        for j, wl in enumerate(head):
            if wl != 'N':
                match_count += 1
            if wl == 'W':
                win_count += 1
                if weights[i] < weights[j]:
                    over_win_count += 1
        if match_count == 0:
            win_rates.append(0)
        else:
            win_rates.append(win_count/match_count)
        over_win_counts.append(over_win_count)
    answer =  sorted(list(range(len(weights))), key=lambda x: (
        win_rates[x], over_win_counts[x], weights[x]
    ), reverse=True)
    return [i+1 for i in answer]


print(solution(weights1, head2head1))
print(solution(weights2, head2head2))
print(solution(weights3, head2head3))