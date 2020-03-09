arrangement = '()(((()())(())()))(())'


### 시간초과
def solution1(arrangement):
    bar = []
    laser = []
    for idx1 in range(len(arrangement)):
        if arrangement[idx1] == '(':
            cnt1 = 1
            cnt2 = 0
            for idx2 in range(len(arrangement[idx1 + 1:])):
                if arrangement[idx1 + 1:][idx2] == ')':
                    cnt2 += 1
                else:
                    cnt1 += 1
                # print(cnt1, cnt2)
                if cnt1 == cnt2:
                    # print('!!!!')
                    if cnt1 == 1:
                        laser.append(idx1)
                    else:
                        bar.append([idx1, idx1 + idx2 + 1])
                    break

    # print(laser, '\n', bar)
    # print(len(arrangement))

    answer = len(bar)
    for l in laser:
        for bar_st, bar_en in bar:
            # print(bar_st, bar_ed, laser)
            if bar_st < l < bar_en:
                answer += 1
            
    # print(answer)
    return answer


def solution(arrangement):
    bar = 0
    answer = 0
    for idx in range(len(arrangement)):
        if arrangement[idx] == '(':
            if arrangement[idx + 1] == ')':
                answer += bar
            else:
                bar += 1
                answer += 1
        else:
            if arrangement[idx - 1] != '(':
                bar -= 1
        # print(idx + 1, '!', bar, answer)

    return answer
    # print(laser, bar, answer)

print(solution(arrangement))