### 1 ###
print('==== 1 ====')
cargo = [1, 3, 1, 5]


def ant(cargo):

    d = []
    for i in range(len(cargo)):
        if i in (0, 1):
            d.append(max(cargo[:i+1]))
        else:
            d.append(max(d[-2]+cargo[i], d[-1]))

    return d[-1]


print(ant(cargo))



### 2 ###
print('==== 2 ====')
n = 26


def cal_int(n):
    cal_list = [n]
    answer = 0
    while 1 not in cal_list:
        answer += 1
        new_cal_list = []
        for i in cal_list:
            if i % 5 == 0:
                new_cal_list.append(i//5)
            if i % 3 == 0:
                new_cal_list.append(i//3)
            if i % 2 == 0:
                new_cal_list.append(i//2)
            new_cal_list.append(i-1)
        cal_list = new_cal_list
    return answer


print(cal_int(n))
print(cal_int(29999))



### 3 ###
print('==== 3 ====')
money1 = [2, 3]; target1 = 15
money2 = [3, 5, 7]; target2 = 4


def cal_money(money, target):
    d = [target+1]*(target+1)
    d[0] = 0

    for m in money:
        if m > target:
            continue
        d[m] = 1
        for i in range(target+1):
            if d[i-m] != target+1:
                d[i] = min(d[i], d[i-m]+1)

    return -1 if d[target] == target+1 else d[target]


print(cal_money(money1, target1))
print(cal_money(money2, target2))



### 4 ###
print('==== 4 ====')
n1 = 3; m1 = 4; gold1 = [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7]
n2 = 4; m2 = 4; gold2 = [1, 3, 1, 5, 2, 2, 4, 1, 5, 0, 2, 3, 0, 6, 1, 2]


def max_gold(n, m, gold):
    new_gold = []
    for i in range(n):
        new_gold.append(gold[i*m:(i+1)*m])

    gold = []
    for g in zip(*new_gold):
        gold.append(list(g))

    for i in range(m-1):
        for j in range(n):
            gold[i+1][j] += max(gold[i][0 if j==0 else j-1:j+2])

    return max(gold[-1])


print(max_gold(n1, m1, gold1))
print(max_gold(n2, m2, gold2))



### 5 ###
print('==== 5 ====')
soldiers = [15, 11, 4, 8, 5, 2, 4]


def out_soldiers(soldiers):
    answer = 1
    for i in range(1, len(soldiers)):
        if soldiers[i-1] > soldiers[i]:
            answer += 1
    return answer


print(out_soldiers(soldiers))
