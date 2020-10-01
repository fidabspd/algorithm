name1 = 'JEROEN'  # 56
name2 = 'JAN'  # 23

def solution(name):

    move = 0
    length = len(name)
    
    for a, b in zip(list(map(ord, name)), [65]*length):
        move += min(a-b, 26-(a-b))  # 상하이동 더하기
    
    not_A = []
    for id, c in enumerate(name):
        if c != 'A':
            not_A.append(id)

    try:
        not_A.remove(0)
    except:
        pass

    now = 0
    while len(not_A) != 1:
        tmp = list(map(abs, [not_A[0]-now, length-abs(not_A[0]-now), not_A[-1]-now, length-abs(not_A[-1]-now)]))
        minimum = min(tmp)
        move += minimum

        if tmp.index(minimum) > 1:  # 좌측이동
            now = not_A[-1]
        else:  # 우측이동
            now = not_A[0]

        not_A.remove(now)
        
    return move + min(abs(now-not_A[0]), length-abs(now-not_A[0]))

print(solution(name))
print(solution(name1))